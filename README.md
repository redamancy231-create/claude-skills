> [English](en/README.md) | 中文 | [正體中文](zh-Hant/README.md)

# Claude Skills

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-8A2BE2)](https://docs.anthropic.com/en/docs/claude-code/skills)
[![Skills](https://img.shields.io/badge/Skills-3-blue)](.)
[![Awesome Skills](https://img.shields.io/badge/featured_in-awesome--skills-brightgreen)](https://github.com/gmh5225/awesome-skills)
[![Featured](https://img.shields.io/badge/featured-Chinese_Independent_Developer-orange)](https://github.com/1c7/chinese-independent-developer)

> **三个经过实战验证的 Claude Code Skill——会话交接、项目文档生成、事前否决审计。**
> 提取自 50+ 轮跨 5 种 LLM 后端的独立审查，来自真实生产项目。

---

## 为什么是这些 Skill？

集合中每个 Skill 都从真实项目工作流中提取——不是在真空中设计。每一个都：

- **实战验证**：经 50+ 轮跨模型独立审查（GPT-5.5 / DeepSeek-V4-Pro / Kimi-K2.7 / Qwen3.7-Max / GLM-5.2）
- **对抗审计**：每个 Skill 发布前都经历了自己的 kill-test
- **可移植**：用户级安装，跨项目通用，无需逐项目配置

| | session-end | write-claude-md | kill-test-first |
|---|---|---|---|
| **类型** | 流程型 | 流程型 | 决策型 |
| **阶段** | 会话结束后 | 项目初始化 | 建设前 |
| **核心问题** | "下个会话需要知道什么？" | "这个 CLAUDE.md 真的帮到 Agent 了吗？" | "这东西值不值得做？" |
| **首次使用时间** | 30 秒 | 5 分钟 | 30 分钟 |

---

## Skills

### 1. session-end — 会话交接标准化执行器

> **"你正在结束一个改变了项目状态的会话。下一个会话必须知道什么？"**

标准化会话交接执行器（基于 AI 协作框架 §9.3）。防止跨会话上下文丢失。

**会话开始检查清单（7 项）：**
- 验证 CLAUDE.md + MEMORY.md 已加载且为最新
- 检查记忆陈旧度（>30 天 → 标记待审查）
- 加载 project_status.md 并确认当前阶段
- 确认环境（Python 版本、工作目录、数据文件可达性）

**会话结束检查清单（5 个模块）：**
- 更新 project_status.md（固定 4 段结构）
- 同步记忆文件（陈旧 ≠ 不准确——交叉检查语义内容，不只是时间戳）
- 捕获跨任务教训 → `memory/*.md`
- 标记 Retrospect 候选（方法论/流程/工具体系发现）
- 写标准化 Next Steps（含优先级 + 依赖关系）

**触发条件：** 产生或改变了项目状态的会话结束时。快问快答（<5 轮，无文件变更）不用。

**文件：** `SKILL.md` · [reference/](session-end/reference/) · [scripts/](session-end/scripts/) · [templates/](session-end/templates/)

---

### 2. write-claude-md — 项目级 CLAUDE.md 编写/优化执行器

> **"对每一行问：删掉它 → Agent 会不会犯错？不会就砍。"**

五步协议——创建或审计项目级 CLAUDE.md 文件。不是模板填空——是结构化审计，问每一行是否真的约束了 Agent 行为。

**五步协议：**

| 步骤 | 内容 | 核心问题 |
|:--:|------|---------------|
| 0 | 上下文收集 | 项目已经告诉了我们什么？ |
| 1 | 脆弱性测试 | 删掉这行 → Agent 会不会搞砸？ |
| 2 | 五缺检查 | 命令、规范、约束、环境、避坑都覆盖了吗？ |
| 3 | 五滥检查 | 是否包含了可推导信息、通用建议、易变数据、文件目录、空泛建议？ |
| 4 | 实证规则 | 白名单指针化、术语显式定义、不维护"最后更新"日期 |
| 5 | 多后端验证 | （重要项目）同 prompt → ≥2 个不同后端 → 收敛/冲突解决 |

**生命周期感知：** 活跃/维护/CLOSED-冻结项目使用不同权重。CLOSED 项目优先记录避坑和重启动指令，而非活跃开发命令。

**文件：** `SKILL.md` · [reference/](write-claude-md/reference/) · [templates/](write-claude-md/templates/)

---

### 3. kill-test-first — 事前否决 + 预登记

> **"最贵的错误不在执行——在那些没人问过'值不值得做'就开始的事情。"**

预登记决策审计——面向新研究方向、量化策略或论文选题。在动工前强制回答"这东西值不值得做？"。

**双门协议：**

```
门1：事前否决（步骤 0→8）
  可证伪命题 → 先验对标 → 最强反方 →
  死亡判据（在看到结果前制定）→ 最便宜证伪 + 强基线 →
  三态裁决：GO / STOP / REDESIGN

门2：预登记冻结（仅当 GO 时）
  冻结协议/指标/判据 → 跑确认性测试 →
  禁止看到数据后挪目标
```

**量化策略红线（6 条不可妥协检查）：**
1. 无泄漏/前视偏差
2. 最强基线比较（不能是稻草人）
3. 清晰的样本外定义
4. 噪声地板/显著性检验
5. 交易成本/容量限制
6. 多重比较校正

**文件：** `SKILL.md` · [reference/](kill-test-first/reference/) · [EXAMPLES.md](kill-test-first/EXAMPLES.md)

---

## 设计思路

- **路由器模式**：SKILL.md 仅含核心流程 + Quick Reference 路由表，详细参考件外置到 `reference/` 目录，Agent 按需读取而非全量加载，控制常驻 Token 消耗
- **渐进式披露**：Skill 主体只暴露入口和触发条件，具体步骤、模板、脚本由 Agent 根据上下文自行路由加载
- **允许工具白名单**：每个 Skill 声明 `allowed-tools`，防止 Agent 在 Skill 上下文中越权操作

## 安装

### 前置要求

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)
- `~/.claude/skills/` 目录（如不存在：`mkdir -p ~/.claude/skills/`）

### 安装全部三个

```bash
git clone https://github.com/redamancy231-create/claude-skills.git
cp -r claude-skills/session-end ~/.claude/skills/
cp -r claude-skills/write-claude-md ~/.claude/skills/
cp -r claude-skills/kill-test-first ~/.claude/skills/
```

### 只装一个

```bash
git clone https://github.com/redamancy231-create/claude-skills.git
cp -r claude-skills/session-end ~/.claude/skills/   # 选你需要的
```

---

## Skill 关系

```
┌──────────────────────────────────────────────────┐
│                  项目生命周期                      │
│                                                  │
│  kill-test-first          write-claude-md         │
│  ┌─────────────┐         ┌──────────────┐        │
│  │ 值不值得做？  │  GO →   │ 为 Agent      │        │
│  │ GO/STOP/    │────────▶│ 记录项目      │        │
│  │ REDESIGN    │         └──────┬───────┘        │
│  └─────────────┘                │                 │
│                                  │                 │
│                    session-end   │                 │
│                    ┌─────────────▼───────────┐    │
│                    │ 把会话状态交接给下一个     │    │
│                    │ 更新 project_status.md   │    │
│                    │ 捕获教训                  │    │
│                    │ 标记 Retrospect           │    │
│                    └─────────────────────────┘    │
└──────────────────────────────────────────────────┘
```

| Skill | 关系 |
|-------|------|
| `kill-test-first` → `write-claude-md` | 重大 CLAUDE.md 重写可选择先过 kill-test |
| `write-claude-md` → `session-end` | 修改 CLAUDE.md 后，session-end 记录变更 |
| `session-end` → `write-claude-md` | write-claude-md 读取 session-end 维护的 `project_status.md` 以检测项目生命周期 |

---

## 相关项目

| 项目 | 关系 |
|------|------|
| [**AI 协作框架**](https://github.com/redamancy231-create/ai-collaboration-framework) | **方法论上游** — 这些 Skill 从框架 §9.2–§9.3 提取，经 50+ 轮跨模型审查 |
| [**Independent Review Toolkit**](https://github.com/redamancy231-create/independent-review-toolkit) | **审查方法来源** — 集合中每个 Skill 均使用该工具包 SOP 进行独立验证 |
| [**Prompt-TDD Methodology**](https://github.com/redamancy231-create/prompt-tdd-methodology) | **同系项目** — kill-test-first 是 prompt-TDD 对照实验协议的直接应用 |
| [**DOCX Pipeline**](https://github.com/redamancy231-create/docx-pipeline) | **同系项目** — Markdown → 中文 DOCX 管道；在其 3 轮审查过程中使用了 session-end 和 write-claude-md |
| [**ETF Pattern Match — pybind11**](https://github.com/redamancy231-create/etf-pattern-match-pybind11) | **同系项目** — C++20/pybind11 量化策略加速；同样应用多模型审查闭合 |
| [**M&A Case Study Pipeline**](https://github.com/redamancy231-create/ma-case-study-pipeline) | **同系项目** — 8 阶段多模型学术生产流水线，含交叉盲审对照实验 |
| [**Awesome Skills**](https://github.com/gmh5225/awesome-skills) | **收录于** — 本 Skill 集合已被 awesome-skills 精选目录收录 |

## 许可

CC BY 4.0 — 详见各 `SKILL.md` frontmatter 中的 per-skill provenance 和验证状态。

## 关于

| | |
|---|---|
| **来源** | 提炼自 [AI 协作框架](https://github.com/redamancy231-create/ai-collaboration-framework) §9.2–§9.3 + 50+ 轮跨模型审查 |
| **审查链** | 每个 Skill 由 ≥2 个不同 LLM 后端独立审查，零卷入设计 |
| **维护者** | [@redamancy231-create](https://github.com/redamancy231-create) |

*由 DeepSeek-V4-Pro (via Claude Code CLI) 生成 · 2026-07-10*
