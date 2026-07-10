# 门1：事前否决（完整协议）

> 从 SKILL.md 拆分。严格按此顺序执行——死亡判据必须早于任何 cheap test/验证结果。

## 0. 独立性声明（先填，决定这次否决算不算数）

- `idea_source`＝谁提出的；`reviewer_是否同一AI/同一会话`＝是/否；`independence_level`＝独立/半独立/非独立。
- ⚠ **若否决官 = 构思者本人 / 同一个 AI / 同一会话**：本次**降级标注为「内部反方检查」，不得声称"独立否决"**。必须在输出末尾强制附一行：`⚠ 本次为非独立检查，建议另起会话 / 换一个模型 / 找人 做一次真正独立的复核`。
- 真独立 = 另起会话 / 另一个模型或 agent / 只给命题与约束不给设计过程 / 人类 reviewer。优先做到一种。

## 1. 可证伪命题

不是「研究 X」，而是「X 满足可被数据推翻的具体断言 Y」。

## 2. 先验对标（prior-art check）— 最便宜的一枪，先于理论反方

⚠ **本关是半天级 prior-art screen，不是 full literature review**；超半天判不清 → 记「检索不足」交人工/第二模型。

### 2.1 术语三角验证
至少换 3 个角度凑查询词——① 你的自然语言说法 ② AI/第二模型给的领域黑话 ③ 某个已知 benchmark/标准的反向术语；至少覆盖 2 类来源。

### 2.2 对抗式检索
「最接近的 3–5 个已有工作是谁」「假设我在重复造轮子，最可能重复了谁」「审稿人会说『这不就是 X 吗』，X 是谁」。

### 2.3 落到可验证源
具名先例必须给 DOI/arXiv/官网/报告页/仓库链接；**AI 只能生成候选、不算最终来源**。搜不到也**不许写「未发现先例」**，只能写「检索不足，记 negative_scope」。

### 2.4 来源验证（强制闸门，P2 新增）

⚠ **GO 之前必须逐条验证先例来源**。对每个具名先例：

| 验证状态 | 判据 | 处理 |
|---------|------|------|
| `verified` | WebFetch/WebSearch 确认链接可访问，且标题/作者匹配 | 可纳入裁决依据 |
| `unverified` | 尝试访问失败（链接失效/需认证/超时），或仅凭模型训练数据回忆 | 标注为 `unverified`，不得单独支撑 GO；需至少 1 条 `verified` |
| `ai-generated` | 无法找到任何外部存在证据（模型可能幻觉了标题/作者/链接） | **立即降级**：从先例列表移除；若全部为 `ai-generated` → 等同「检索不足」→ 不得 GO |

- 验证工具：优先 `WebFetch`（确认链接可达）+ `WebSearch`（交叉确认标题/作者匹配）。
- 若 `verified` 先例为 0 条 → 不得 GO，必须标记 `⚠ prior_art_unverified`。
- 输出中须逐条标注验证状态及所使用的验证方法。

### 2.5 差异判定
拿 **核心问题 / 输出物 / 评估指标** 三项比先例——三项高度重合、且新增差异不能改变用户决策 → **REDESIGN** 或 STOP；差异能形成可证伪新命题 → 继续，但**把先例写进命题 + baseline**。

⚠ **对标通过 ≠ 最强反方通过**：步骤 3 仍为必填。

## 3. 最强反方论证

站在「注定不成」立场给最锋利的理论 kill（针对**核心机制**，非边角）。

## 4. 死亡判据（在看到任何结果之前写死）

**这一步在跑实验之前**——顺序错了，预登记就废了。

## 5. cheap test 设计

用最小成本的检验，先于全面建设。

## 6. cheap test 质量门槛（运行前必过）

样本量是否够、代理指标是否贴合核心命题、实现复核、噪声底、最小可解释效应；**基线非 strawman、泄漏/未来函数**见 [quant-redlines.md](quant-redlines.md)。任一不过 → REDESIGN。

## 6.5. 可复现性预检

- **代码完整性**：原始数据→训练/分析数据的每一步转换是否有对应代码？
- **参数显式可追溯**：过滤阈值/采样参数/配对规则/随机种子是否显式可追溯？
- **端到端 smoke test**：是否包含最小可运行示例？
- **版本绑定**：论文版本与代码版本是否绑定？
- 任一为"否"→ 标注 `⚠ reproducibility_precheck`，cheap test 可信度降级。

## 7. 运行 → 结果

## 8. 三态裁决（GO 要求质量门槛逐项全过）

- **STOP**：质量门槛已过 **且** cheap test 证伪 → 不进 Phase 1。
- **REDESIGN**：质量不达标 / 功效不足 / 代理失真 → 重写命题或换检验。⚠ **同一命题 REDESIGN 累计 ≤ 2 次**；第 3 次必须升级为 STOP 或提交人工决策。
- **GO**：cheap test 未证伪 **且** 质量门槛**逐项全过** → 进入下一阶段，死亡判据全程挂着。GO ≠「值得大建」。

---

## 固定输出块

```
【核心块 · 每次必填】
Independence Declaration: idea_source / same_agent / independence_level
  ↳ 若 same_agent=是 → 强制附：⚠ 本次非独立...
Falsifiable Claim:
Prior-Art Check (缺项判不合格、不得 GO):
  术语试了哪几组(≥3角度) / 查了哪些源(≥2类) / 最近 3-5 个先例(具名+可验证链接) /
  来源验证(逐条: verified/unverified/ai-generated + 验证方法) /   ← P2 新增
  我 vs 先例差异(核心问题·输出物·评估指标) / 裁决
Strongest Contra:
Kill Criteria (BEFORE results):        ← 必须早于下面 Result
Cheap Test Design:
Quality Checks:
已看过任何结果？ yes/no                 ← yes 则标 retrospective
Result:
Decision: GO / STOP / REDESIGN          ← 若 REDESIGN：本命题累计第几次（≤2）
Self-check: Prior-Art/Contra/Kill Criteria 是否达「最低合格标准」？

【门2块 · 仅 Decision=GO 后填】
已冻结新 holdout / 时间切片 / 外部数据？
谁冻结 / 冻结时间:
触发 amendment？ 原因（须非因结果）:
```
