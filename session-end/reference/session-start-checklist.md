# Session Start 检查清单

> 从 SKILL.md 拆分。Claude Code 启动时已自动读 CLAUDE.md + MEMORY.md，本清单做**复核**非重复读取。
> ⚠ **输出规则**：以下带"复核"字样的确认型检查项，**必须输出具体值**而非仅打勾——例如报告实际读到的路径/版本/数量，含"✓"或"⚠"判定。禁止无声通过。

**前置：确认当前项目** — 从 CWD 或对话上下文确定项目根目录。如 CWD 不在项目目录内，从 CLAUDE.md 或 memory 中的 `reference_project_paths.md` 查找项目路径。

> ⚠ **跳过规则**：Session Start 清单的复核项在以下情况可跳过——(a) 同一会话内第二次及之后调用 `/session-end`；(b) 短会话（<10 轮、未切换项目）且用户已确认上下文未压缩。此时仅执行 Session End 清单。

- [ ] **复核 CLAUDE.md**：输出实际读取的项目路径 + 版本号，与当前任务比对后标 ✓ 或 ⚠
- [ ] **复核 MEMORY.md**：输出索引条目总数 + 本次会话已知的新增/删除条目数（如有）
- [ ] **逐条检查 memory 时效性**：超过 **30 天**的条目 → 列出文件名+最后更新日，提醒"需验证"；全部新鲜则报告"memory 全部在 30 天内（N 条）"。快捷命令：
  ```bash
  PYTHONIOENCODING=utf-8 python scripts/check-memory-staleness.py
  ```
  也可用内嵌片段（见 `scripts/check-memory-staleness.py` 源码）。
- [ ] **读本项目 project_status.md**（如不存在 → 用固定模板 `## 项目状态: [项目名]\n\n- 当前阶段: 初始化\n- 本轮完成: 项目启动\n- 发现的问题: 无` 创建）：输出当前阶段+已知问题数+未完成 Next Steps 数
- [ ] **检查未完成 Next Steps**：逐条确认是否仍相关、依赖是否已满足、优先级是否需要调整；无未完成任务则明确标注"无"
- [ ] **读上次 Retrospect**（如有；通常位于项目 `_reviews/` 目录下，文件名含 `retrospect` 关键词；如不存在则标注"无 Retrospect"）：未处理的发现/教训/整改项？
- [ ] **确认当前环境**：输出具体值 — `python --version` 结果 + 项目要求版本 + ✓/⚠；工作目录绝对路径；如项目涉及数据文件，输出关键数据文件路径+可读性（✓/⚠）
