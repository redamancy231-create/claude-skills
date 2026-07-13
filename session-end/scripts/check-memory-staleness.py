"""检查 memory 目录中超过 30 天未更新的文件。

从 session-end Session Start 清单中提取，改为独立脚本以便跨平台复用。
通过环境变量 CLAUDE_MEMORY_DIR 指定 memory 目录路径（必设）。

跳过规则（不报告为过期）：
- frontmatter metadata.status 含 CLOSED / CLOSED-FINAL / CLOSED-ARCHIVED / ARCHIVED（已封存/关闭项目）
- frontmatter metadata 含 staleness_check: false（显式标记为稳定内容，如硬件规格/待用户行动的诊断记录）
"""
import os
import re
import sys
import time

MEMORY_DIR = os.environ.get("CLAUDE_MEMORY_DIR", "")

if not MEMORY_DIR:
    print("❌ 请设置环境变量 CLAUDE_MEMORY_DIR 指向 memory 目录")
    sys.exit(1)

MEMORY_DIR = os.path.expanduser(MEMORY_DIR)

CUTOFF_DAYS = int(os.environ.get("CLAUDE_MEMORY_STALE_DAYS", "30"))

# frontmatter metadata.status 值命中任一项 → 跳过过期检查
SKIP_STATUS_VALUES = {"CLOSED", "CLOSED-FINAL", "CLOSED-ARCHIVED", "ARCHIVED"}


def parse_skip_flags(filepath: str):
    """Parse frontmatter for staleness skip signals. Returns (skip: bool, reason: str)."""
    try:
        with open(filepath, "r", encoding="utf-8") as fh:
            content = fh.read(2048)  # frontmatter is always at the top
    except Exception:
        return False, ""

    # Extract YAML frontmatter between --- delimiters
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return False, ""

    frontmatter = match.group(1)

    # Check staleness_check: false (anchored to line start to avoid matching inside description strings)
    if re.search(r"^\s*staleness_check\s*:\s*false", frontmatter, re.MULTILINE):
        return True, "staleness_check=false"

    # Check status field for CLOSED/ARCHIVED variants (line-anchored, same reason)
    status_match = re.search(r"^\s*status\s*:\s*(\S.*)", frontmatter, re.MULTILINE)
    if status_match:
        raw = status_match.group(1).strip()
        # Handle quoted and unquoted values
        status_val = raw.strip("'\"").split()[0].rstrip(",")
        if status_val.upper() in SKIP_STATUS_VALUES or status_val in SKIP_STATUS_VALUES:
            return True, f"status={status_val}"

    return False, ""


def main():
    if not os.path.isdir(MEMORY_DIR):
        print(f"⚠ memory 目录不存在: {MEMORY_DIR}")
        sys.exit(1)

    cutoff = time.time() - CUTOFF_DAYS * 86400
    stale = []
    skipped = []

    for f in sorted(os.listdir(MEMORY_DIR)):
        if f.endswith(".md") and f != "MEMORY.md":
            fp = os.path.join(MEMORY_DIR, f)
            mtime = os.path.getmtime(fp)
            if mtime < cutoff:
                skip, reason = parse_skip_flags(fp)
                if skip:
                    skipped.append((f, reason))
                else:
                    days = int((time.time() - mtime) / 86400)
                    stale.append((f, days))

    if skipped:
        for name, reason in skipped:
            print(f"  ⏭ {name} (跳过: {reason})")

    if stale:
        for name, days in sorted(stale, key=lambda x: -x[1]):
            print(f"  ⚠ {name} ({days}d)")
    else:
        print(f"  ✅ 需人工复查的 memory 全部在 {CUTOFF_DAYS} 天内 ({MEMORY_DIR})")


if __name__ == "__main__":
    main()
