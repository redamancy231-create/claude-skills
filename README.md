# Claude Skills

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-8A2BE2)](https://docs.anthropic.com/en/docs/claude-code/skills)
[![Codex](https://img.shields.io/badge/Codex-compatible-10A37F)](https://developers.openai.com/codex/skills)
[![Skills](https://img.shields.io/badge/Skills-3-blue)](.)
[![Awesome Skills](https://img.shields.io/badge/featured_in-awesome--skills-brightgreen)](https://github.com/gmh5225/awesome-skills)
[![Featured](https://img.shields.io/badge/featured-chinese--independent--developer-orange)](https://github.com/1c7/chinese-independent-developer)

> **Battle-tested Claude Code Skills for session handoff, project documentation, and decision audit.**
> Derived from 50+ rounds of cross-model independent review across 5 LLM backends in production projects.
> Compatible with Claude Code, Codex, Cursor, and Gemini CLI.

---

## Why these skills?

Every skill in this collection was extracted from real project workflows — not designed in a vacuum. Each one:

- **Field-verified** through 50+ rounds of multi-model independent review (GPT-5.5 / DeepSeek-V4-Pro / Kimi-K2.7 / Qwen3.7-Max / GLM-5.2)
- **Adversarially audited** — each skill underwent its own kill-test before being published
- **Portable** — user scope, works across projects without per-project configuration

| | session-end | write-claude-md | kill-test-first |
|---|---|---|---|
| **Type** | Workflow | Workflow | Decision |
| **Phase** | Post-session | Project setup | Pre-build |
| **Core question** | "What does the next session need to know?" | "Does this CLAUDE.md actually help the agent?" | "Should we even build this?" |
| **Time to first use** | 30 seconds | 5 minutes | 30 minutes |

---

## Skills

### 1. session-end — 会话交接标准化执行器

> **"You're ending a session that changed project state. What must the next session know?"**

Standardized handoff executor per AI collaboration framework §9.3. Prevents context loss across sessions.

**Session Start checklist (7 items):**
- Verify CLAUDE.md + MEMORY.md loaded and current
- Check memory staleness (>30d → flag for review)
- Load project_status.md and confirm current phase
- Confirm environment (Python version, working directory, data file accessibility)

**Session End checklist (5 modules):**
- Update project_status.md with fixed 4-section structure
- Sync memory files (staleness ≠ accuracy — cross-check semantic content, not just timestamps)
- Capture cross-task lessons → `memory/*.md`
- Flag Retrospect candidates (methodology/process/tooling discoveries)
- Write standardized Next Steps with priority + dependencies

**When to use:** Ending a session that produced or changed project state. Not for quick Q&A (<5 turns, no file changes).

**Files:** `SKILL.md` · [reference/](session-end/reference/) · [scripts/](session-end/scripts/) · [templates/](session-end/templates/)

---

### 2. write-claude-md — 项目级 CLAUDE.md 编写/优化执行器

> **"For every line: delete it → would the agent make a mistake? If not, cut it."**

Five-step protocol for creating or auditing project-level CLAUDE.md files. Not a template filler — a structured audit that asks whether each line actually constrains agent behavior.

**Five-step protocol:**

| Step | What | Core question |
|:--:|------|---------------|
| 0 | Context collection | What does the project already tell us? |
| 1 | Vulnerability testing | Delete this line → would the agent break something? |
| 2 | Five-gap check | Are critical commands, conventions, constraints, environment, and pitfalls all covered? |
| 3 | Five-abuse check | Are we including derivable info, generic advice, volatile data, file catalogs, or empty suggestions? |
| 4 | Empirical rules | Whitelist-pointerization, explicit terminology, no last-updated dates |
| 5 | Multi-backend validation | (Important projects) Same prompt → ≥2 different backends → converge/conflict resolution |

**Lifecycle-aware:** Different weights for active vs. maintenance vs. CLOSED/frozen projects. CLOSED projects prioritize pitfall documentation and restart instructions over active development commands.

**Files:** `SKILL.md` · [reference/](write-claude-md/reference/) · [templates/](write-claude-md/templates/)

---

### 3. kill-test-first — 事前否决 + 预登记

> **"The most expensive mistakes aren't in execution — they're in things nobody asked 'should we?' before starting."**

Pre-registration decision audit for new research directions, quant strategies, or thesis topics. Forces the question "should we build this?" before any building happens.

**Two-gate protocol:**

```
Gate 1: Pre-build Veto (Steps 0→8)
  Falsifiable claim → Prior-art check → Strongest counter-argument →
  Death criteria (BEFORE seeing results) → Cheapest falsification with strong baseline →
  Three-state verdict: GO / STOP / REDESIGN

Gate 2: Pre-registration Freeze (only if GO)
  Freeze protocol/metrics/kill-criteria before confirmatory testing →
  No moving goalposts after seeing data
```

**Quant strategy redlines (6 non-negotiable checks):**
1. No leakage / look-ahead bias
2. Strongest baseline comparison (not a strawman)
3. Clear out-of-sample definition
4. Noise floor / significance testing
5. Transaction costs / capacity limits
6. Multiple comparison correction

**Files:** `SKILL.md` · [reference/](kill-test-first/reference/) · [EXAMPLES.md](kill-test-first/EXAMPLES.md)

---

## Installation

### Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) (or Codex, Cursor, Gemini CLI)
- `~/.claude/skills/` directory (create if missing: `mkdir -p ~/.claude/skills/`)

### Install all three

```bash
git clone https://github.com/redamancy231-create/claude-skills.git
cp -r claude-skills/session-end ~/.claude/skills/
cp -r claude-skills/write-claude-md ~/.claude/skills/
cp -r claude-skills/kill-test-first ~/.claude/skills/
```

### Install just one

```bash
git clone https://github.com/redamancy231-create/claude-skills.git
cp -r claude-skills/session-end ~/.claude/skills/   # pick the one you need
```

---

## Skill relationships

```
┌──────────────────────────────────────────────────┐
│                  Project lifecycle                │
│                                                  │
│  kill-test-first          write-claude-md         │
│  ┌─────────────┐         ┌──────────────┐        │
│  │ Should we    │  GO →   │ Document the  │        │
│  │ build this?  │────────▶│ project for   │        │
│  │ GO/STOP/     │         │ the agent     │        │
│  │ REDESIGN     │         └──────┬───────┘        │
│  └─────────────┘                │                 │
│                                  │                 │
│                    session-end   │                 │
│                    ┌─────────────▼───────────┐    │
│                    │ Hand off session state   │    │
│                    │ to the next session      │    │
│                    │ Update project_status.md │    │
│                    │ Capture lessons          │    │
│                    │ Flag Retrospects         │    │
│                    └─────────────────────────┘    │
└──────────────────────────────────────────────────┘
```

| Skill | Relationship |
|-------|-------------|
| `kill-test-first` → `write-claude-md` | Major CLAUDE.md rewrites can optionally pass kill-test before execution |
| `write-claude-md` → `session-end` | After modifying CLAUDE.md, session-end records the change |
| `session-end` → `write-claude-md` | write-claude-md reads `project_status.md` (maintained by session-end) for lifecycle detection |

---


## Related Projects

| Project | Relationship |
|------|------|
| [**AI Collaboration Framework**](https://github.com/redamancy231-create/ai-collaboration-framework) | **Methodology upstream** — these skills were extracted from the framework (§9.2–§9.3) after 50+ rounds of cross-model review |
| [**Independent Review Toolkit**](https://github.com/redamancy231-create/independent-review-toolkit) | **Review methodology source** — each skill in this collection was independently validated using the toolkit's SOP |
| [**Prompt-TDD Methodology**](https://github.com/redamancy231-create/prompt-tdd-methodology) | **Sibling project** — kill-test-first is a direct application of the prompt-TDD controlled experiment protocol |
| [**DOCX Pipeline**](https://github.com/redamancy231-create/docx-pipeline) | **Sibling project** — Markdown → Chinese DOCX pipeline; used session-end and write-claude-md skills during its own 3-round review process |
| [**Awesome Skills**](https://github.com/gmh5225/awesome-skills) | **Featured in** — this skill collection is listed in the awesome-skills curated directory of agent skills |

<details>
<summary>中文</summary>

| 项目 | 关系 |
|------|------|
| [**AI 协作框架**](https://github.com/redamancy231-create/ai-collaboration-framework) | **方法论上游** — 这些 Skill 从框架 §9.2–§9.3 提取，经 50+ 轮跨模型审查 |
| [**Independent Review Toolkit**](https://github.com/redamancy231-create/independent-review-toolkit) | **审查方法来源** — 集合中每个 Skill 均使用该工具包 SOP 进行独立验证 |
| [**Prompt-TDD Methodology**](https://github.com/redamancy231-create/prompt-tdd-methodology) | **同系项目** — kill-test-first 是 prompt-TDD 对照实验协议的直接应用 |
| [**DOCX Pipeline**](https://github.com/redamancy231-create/docx-pipeline) | **同系项目** — Markdown → 中文 DOCX 泛化管道；在其 3 轮审查过程中使用了 session-end 和 write-claude-md |
| [**Awesome Skills**](https://github.com/gmh5225/awesome-skills) | **收录于** — 本 Skill 集合已被 awesome-skills 精选目录收录 |

</details>

## License

CC BY 4.0 — see individual `SKILL.md` frontmatter for per-skill provenance and verification status.

## About

| | |
|---|---|
| **Source** | Extracted from [AI Collaboration Framework](https://github.com/redamancy231-create/ai-collaboration-framework) §9.2–§9.3 + 50+ rounds of cross-model review |
| **Review chain** | Each skill independently reviewed by ≥2 different LLM backends with zero involvement in design |
| **Maintainer** | [@redamancy231-create](https://github.com/redamancy231-create) |

*Generated by DeepSeek-V4-Pro (via Claude Code CLI) · 2026-07-10*

<br>

<details>
<summary><b>中文</b></summary>

## Claude Skills · 中文说明

> 三个经过实战验证的 Claude Code Skill，提取自 50+ 轮跨模型独立审查的生产项目。

### 项目定位

这不是"教程示例"——每个 Skill 都从真实项目工作流中提取，经过异后端独立审查闭合。

| | session-end | write-claude-md | kill-test-first |
|---|---|---|---|
| **类型** | 流程型 | 流程型 | 决策型 |
| **阶段** | 会话结束后 | 项目初始化 | 建设前 |
| **核心问题** | "下个会话需要知道什么？" | "这个 CLAUDE.md 真的帮到 Agent 了吗？" | "这东西值不值得做？" |

### session-end · 会话交接

标准化会话交接执行器。确保跨会话状态可恢复——更新 project_status.md、捕获跨任务教训、标记 Retrospect 候选、写标准化 Next Steps。触发条件：产生项目状态变更的实质性会话结束时。

### write-claude-md · 编写 CLAUDE.md

五步协议：证据采集 → 脆弱性测试（每行都问"删掉会不会犯错"）→ 五缺检查 → 五滥检查 → 可选多后端验证。区分活跃/维护/冻结项目的差异化权重。

### kill-test-first · 事前否决

两门协议——门1 事前否决（可证伪命题 → 先验对标 → 最强反方 → 死亡判据 → 最便宜证伪 → GO/STOP/REDESIGN），门2 预登记冻结。量化策略含 6 条不可外包红线。

### 安装

```bash
git clone https://github.com/redamancy231-create/claude-skills.git
cp -r claude-skills/session-end ~/.claude/skills/
cp -r claude-skills/write-claude-md ~/.claude/skills/
cp -r claude-skills/kill-test-first ~/.claude/skills/
```

### 出处

提炼自 [AI 协作框架](https://github.com/redamancy231-create/ai-collaboration-framework) §9.2–§9.3。CC BY 4.0。

</details>