# Step 0：上下文采集

> 从 SKILL.md 拆分。采集项目既有信息，为后续审计提供证据基础。

读取以下文件（存在则读，不存在则跳过）：
- `[ ]` 现有 `CLAUDE.md`（如审计模式）
- `[ ]` `README.md`（项目类型、技术栈、命令入口）
- `[ ]` 构建/包管理配置（`package.json`/`pyproject.toml`/`Cargo.toml`/`go.mod` 等）
- `[ ]` `.gitignore`（发布边界）
- `[ ]` `VERSION`（如有）
- `[ ]` 主要入口文件（`main.py`/`index.js`/`src/` 结构等）
- `[ ]` `project_status.md`（如有——获取当前阶段和待办）

**退出条件**：命令无法验证 → 标注"需确认"或询问用户。项目类型不明确 → 询问用户。
