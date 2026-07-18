> [简体中文](../README.md) | English | [正體中文](../zh-Hant/README.md)

# Claude Skills

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-8A2BE2)](https://docs.anthropic.com/en/docs/claude-code/skills)
[![Skills](https://img.shields.io/badge/Skills-3-blue)](..)
[![Awesome Skills](https://img.shields.io/badge/featured_in-awesome--skills-brightgreen)](https://github.com/gmh5225/awesome-skills)
[![Featured](https://img.shields.io/badge/featured-Chinese_Independent_Developer-orange)](https://github.com/1c7/chinese-independent-developer)
[![简体中文](https://img.shields.io/badge/README-简体中文-red)](../README.md) [![English](https://img.shields.io/badge/README-English-blue)](.) [![正體中文](https://img.shields.io/badge/README-正體中文-orange)](../zh-Hant/README.md)

> **Battle-tested Claude Code Skills for session handoff, project documentation, and decision audit.**
> Derived from 50+ rounds of cross-model independent review across 5 LLM backends in production projects.

---

## Why these skills?

Every skill in this collection was extracted from real project workflows — not designed in a vacuum. Each one:

- **Field-verified** — each skill independently reviewed by ≥2 different LLM backends; the framework as a whole underwent 50+ rounds of cross-model verification (GPT-5.5 / DeepSeek-V4-Pro / Kimi-K2.7 / Qwen3.7-Max / GLM-5.2)
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

### 1. session-end — Standardized Session Handoff Executor

> **"You're ending a session that changed project state. What must the next session know?"**

Standardized handoff executor per AI collaboration framework §9.3. Prevents context loss across sessions.

**Session Start checklist (4 of 7 items shown):**
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

**Files:** `SKILL.md` · [reference/](../session-end/reference/) · [scripts/](../session-end/scripts/) · [templates/](../session-end/templates/)

---

### 2. write-claude-md — Project CLAUDE.md Generator / Auditor

> **"For every line: delete it → would the agent make a mistake? If not, cut it."**

Five-step protocol for creating or auditing project-level CLAUDE.md files. Not a template filler — a structured audit that asks whether each line actually constrains agent behavior.

**Step 0 + five-step protocol:**

| Step | What | Core question |
|:--:|------|---------------|
| 0 | Context collection | What does the project already tell us? |
| 1 | Vulnerability testing | Delete this line → would the agent break something? |
| 2 | Five-gap check | Are critical commands, conventions, constraints, environment, and pitfalls all covered? |
| 3 | Five-abuse check | Are we including derivable info, generic advice, volatile data, file catalogs, or empty suggestions? |
| 4 | Empirical rules | Whitelist-pointerization, explicit terminology, no last-updated dates |
| 5 | Multi-backend validation | (Important projects) Same prompt → ≥2 different backends → converge/conflict resolution |

**Lifecycle-aware:** Different weights for active vs. maintenance vs. CLOSED/frozen projects. CLOSED projects prioritize pitfall documentation and restart instructions over active development commands.

**Files:** `SKILL.md` · [reference/](../write-claude-md/reference/) · [templates/](../write-claude-md/templates/)

---

### 3. kill-test-first — Pre-Registration Decision Audit

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

**Files:** `SKILL.md` · [reference/](../kill-test-first/reference/) · [EXAMPLES.md](../kill-test-first/EXAMPLES.md)

---

## Design Philosophy

- **Router Pattern**: SKILL.md contains only the core workflow + Quick Reference routing table; detailed reference files are placed in `reference/` directories for on-demand loading, keeping resident token consumption under control
- **Progressive Disclosure**: The skill body exposes only entry points and trigger conditions; specific steps, templates, and scripts are loaded by the agent based on context
- **Allowed-Tools Whitelist**: Each skill declares `allowed-tools`, preventing the agent from performing unauthorized operations within skill context

## Installation

### Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)
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
| [**DOCX Pipeline**](https://github.com/redamancy231-create/docx-pipeline) | **Sibling project** — Markdown → Chinese DOCX pipeline; used session-end and write-claude-md during its own 3-round review process |
| [**ETF Pattern Match — pybind11**](https://github.com/redamancy231-create/etf-pattern-match-pybind11) | **Sibling project** — C++20/pybind11 quant strategy acceleration; similarly applies multi-model review closure |
| [**M&A Case Study Pipeline**](https://github.com/redamancy231-create/ma-case-study-pipeline) | **Sibling project** — 8-stage multi-model academic production pipeline with cross-blind review |
| [**Awesome Skills**](https://github.com/gmh5225/awesome-skills) | **Featured in** — this skill collection is listed in the awesome-skills curated directory of agent skills |

## License

CC BY 4.0 — see individual `SKILL.md` frontmatter for per-skill provenance and verification status.

## About

| | |
|---|---|
| **Source** | Extracted from [AI Collaboration Framework](https://github.com/redamancy231-create/ai-collaboration-framework) §9.2–§9.3 + 50+ rounds of cross-model review |
| **Review chain** | Each skill independently reviewed by ≥2 different LLM backends with zero involvement in design |
| **Maintainer** | [@redamancy231-create](https://github.com/redamancy231-create) |

*Generated by DeepSeek-V4-Pro (via Claude Code CLI) · 2026-07-10*
