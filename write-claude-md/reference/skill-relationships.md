# 与其他 Skill 的关系

> 从 SKILL.md 拆分。

| Skill | 关系 | 串联 |
|-------|------|------|
| `session-end` | session-end 更新 `project_status.md`（含当前阶段/待办/模型可用列表）；write-claude-md 引用 `project_status.md` 作为白名单指针目标 | 修改 CLAUDE.md 后 → session-end 记录变更 |
| `kill-test-first` | kill-test 管事前否决（"这个 CLAUDE.md 改动该不该做"）；write-claude-md 管执行质量 | 重大 CLAUDE.md 重写前可选跑 kill-test |
| `write-a-skill` | 项目专业领域知识超 200 行或需要按需加载 → 迁移至 Skill，不堆在 CLAUDE.md | CLAUDE.md 引用 Skill 名称和触发条件 |
