"""检查 memory 目录中超过 30 天未更新的文件。

从 session-end Session Start 清单中提取，改为独立脚本以便跨平台复用。
通过环境变量 CLAUDE_MEMORY_DIR 指定 memory 目录路径（必设）。
"""
import os
import sys
import time

MEMORY_DIR = os.environ.get("CLAUDE_MEMORY_DIR", "")

if not MEMORY_DIR:
    print("❌ 请设置环境变量 CLAUDE_MEMORY_DIR 指向 memory 目录")
    sys.exit(1)

MEMORY_DIR = os.path.expanduser(MEMORY_DIR)

CUTOFF_DAYS = int(os.environ.get("CLAUDE_MEMORY_STALE_DAYS", "30"))


def main():
    if not os.path.isdir(MEMORY_DIR):
        print(f"⚠ memory 目录不存在: {MEMORY_DIR}")
        sys.exit(1)

    cutoff = time.time() - CUTOFF_DAYS * 86400
    stale = []

    for f in os.listdir(MEMORY_DIR):
        if f.endswith(".md") and f != "MEMORY.md":
            fp = os.path.join(MEMORY_DIR, f)
            mtime = os.path.getmtime(fp)
            if mtime < cutoff:
                days = int((time.time() - mtime) / 86400)
                stale.append((f, days))

    if stale:
        for name, days in sorted(stale, key=lambda x: -x[1]):
            print(f"  ⚠ {name} ({days}d)")
    else:
        print(f"  ✅ all memory in {CUTOFF_DAYS} days ({MEMORY_DIR})")


if __name__ == "__main__":
    main()
