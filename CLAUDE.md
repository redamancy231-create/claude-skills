# CLAUDE.md — claude-skills

> 非软件项目（Markdown 文档集合）：3 个 Claude Code Skill + 三语 README + 参考件/模板/脚本。
> 生命周期：**CLOSED**（v1.0.1，脱敏闭合）。

## Agent 边界

**允许（无需确认）**：
- 读取/搜索项目文件（Read、Glob、Grep）
- 修改 SKILL.md 中的描述文本、路由表条目、触发条件措辞（不改变 Skill 架构）
- 修改 `reference/` 下的参考文件内容
- 修改 README.md / CHANGELOG.md
- 三语 README 之间的同步修正

**需先确认**：
- 新增/删除 Skill（改变项目范围）
- 修改 YAML frontmatter 中的 `allowed-tools` 或 `verified_by`（改变安全边界或审查声明）
- 改变 SKILL.md 的架构（如拆分/合并路由表）

**禁止**：
- 修改 `_review/` 目录下的审查记录（历史证据，只读）
- 声称"已验证"或"已测试"（本机无 Claude Code 运行环境，无法实际验证 Skill 行为）
- 全量重写已有 SKILL.md（审计模式——增量修改，禁止全量重写）

## 关键约束

### 修改 SKILL.md 后的同步链

修改任一 `SKILL.md` 后，必须检查以下文件是否需要同步：

1. `README.md` — 如变更影响"Skills"章节的描述或路由表示例
2. `en/README.md` — 英文翻译的对应段落
3. `zh-Hant/README.md` — 正體中文翻译的对应段落
4. `CHANGELOG.md` — 如有用户可见的变更
5. `project_status.md` — 如变更代表项目状态或版本变化

**同步检查方法**：修改后 grep 被修改的关键术语/字段名，确认三语 README 中对应行已更新。

### 多语言 README 关系

| 文件 | 角色 | 维护规则 |
|------|------|---------|
| `README.md`（根） | **主版本**（简体中文） | 所有修改先在此文件执行 |
| `en/README.md` | 英文翻译 | 从主版本翻译，非独立创作 |
| `zh-Hant/README.md` | 正體中文 | OpenCC 简→繁转换 + 人工校对术语 |

**禁止**：在 `en/` 或 `zh-Hant/` 中直接创作新内容而不更新根 README——会导致三语版本漂移。

### Skill 架构不变量

三个 Skill 共享以下设计约束（路由器模式——不可单方面打破）：
- SKILL.md ≤ 100 行（核心流程 + 路由表）
- 详细件外置到 `reference/` 目录，通过路由表索引
- YAML frontmatter 必须包含 `name`、`description`、`allowed-tools`、`verified_by`
- 每个 Skill 必须有 `reference/death-criteria.md`

## 环境与命令

```bash
# 检查三语 README 术语同步（以关键术语 grep 三语文件）
grep -n "路由器模式\|渐进式披露\|allowed-tools" README.md en/README.md zh-Hant/README.md

# 统计 SKILL.md 行数（不应超过 100 行）
wc -l */SKILL.md

# 检查 YAML frontmatter 完整性（name/description/allowed-tools/verified_by 四个必填字段）
for f in */SKILL.md; do echo "=== $f ==="; head -10 "$f" | grep -E "^(name|description|allowed-tools|verified_by):"; done
```

## 已知坑位

| 坑 | 后果 | 预防 |
|----|------|------|
| 改 SKILL.md 后只更新了根 README，漏了 `en/` 和 `zh-Hant/` | 三语版本漂移——用户看到过期信息 | 修改后用上面的 grep 检查三语同步 |
| 改 SKILL.md 架构但 README 路由表示例未同步 | README 展示的用法与实际 SKILL.md 不一致 | 修改涉及路由表 → 必查 README 对应示例 |
| 在英文 README 中直接写新内容 | 英文版与中文版内容分化，后续维护成本翻倍 | 新内容一律先在根 README 写，再翻译 |
| YAML frontmatter 字段缺失或格式错误 | Skill 注册失败或 allowed-tools 不生效 | 用上面的 frontmatter 完整性检查命令 |
| CLAUDE.md 自身的 SKILL.md 修改 | 本项目的 write-claude-md Skill 和自身 CLAUDE.md 形成递归——改协议后自己的 CLAUDE.md 也要同步 | 改 write-claude-md 后立即审查本项目 CLAUDE.md |

## 停止条件

1. 任何操作会破坏三语 README 的对应关系 → 停止，先确认同步策略
2. 修改会使 SKILL.md 超过 100 行 → 停止，先讨论是否需要重构路由表
3. 提议删除或实质性削弱 `reference/death-criteria.md` → 停止（这是 Skill 质量保障的核心机制）
4. 提议在 `en/` 或 `zh-Hant/` 中独立创作新内容 → 停止（先更新根 README）

## 更新协议

### 版本号规则
- v1.0.x：脱敏/措辞/同步修正（不改变 Skill 功能）
- v1.x.0：Skill 架构变化或新增 Skill
- 详见 `CHANGELOG.md`

### 修改后必做
1. 更新 `CHANGELOG.md`
2. 运行三语同步检查命令
3. 更新 `project_status.md` 的"本轮完成"字段
4. 如有新增审查 → 审查记录存入 `_review/`（不提交到仓库）

### 重启指南
项目 v1.0.1 已脱敏闭合。如需重启（新增 Skill 或重大架构变更）：
1. 先读 `session-end/reference/lessons.md` — 了解历史上踩过的坑
2. 先读 `write-claude-md/reference/anti-patterns.md` — 避免已知反模式
3. 新 Skill 必须先过 `kill-test-first` 的事前否决（双门协议）
4. 发布前 ≥2 个异后端独立审查
