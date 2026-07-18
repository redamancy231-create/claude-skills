> [簡體中文](../README.md) | [English](../en/README.md) | 正體中文

# Claude Skills

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-8A2BE2)](https://docs.anthropic.com/en/docs/claude-code/skills)
[![Skills](https://img.shields.io/badge/Skills-3-blue)](..)
[![Awesome Skills](https://img.shields.io/badge/featured_in-awesome--skills-brightgreen)](https://github.com/gmh5225/awesome-skills)
[![Featured](https://img.shields.io/badge/featured-Chinese_Independent_Developer-orange)](https://github.com/1c7/chinese-independent-developer)
[![简体中文](https://img.shields.io/badge/README-簡體中文-red)](.) [![English](https://img.shields.io/badge/README-English-blue)](en/README.md) [![正體中文](https://img.shields.io/badge/README-正體中文-orange)](zh-Hant/README.md)

> **三個經過實戰驗證的 Claude Code Skill——會話交接、項目文檔生成、事前否決審計。**
> 提取自 50+ 輪跨 5 種 LLM 後端的獨立審查，來自真實生產項目。

---

## 為什麼是這些 Skill？

集合中每個 Skill 都從真實項目工作流中提取——不是在真空中設計。每一個都：

- **實戰驗證**：經 50+ 輪跨模型獨立審查（GPT-5.5 / DeepSeek-V4-Pro / Kimi-K2.7 / Qwen3.7-Max / GLM-5.2）
- **對抗審計**：每個 Skill 發佈前都經歷了自己的 kill-test
- **可移植**：用戶級安裝，跨項目通用，無需逐項目配置

| | session-end | write-claude-md | kill-test-first |
|---|---|---|---|
| **類型** | 流程型 | 流程型 | 決策型 |
| **階段** | 會話結束後 | 項目初始化 | 建設前 |
| **核心問題** | "下個會話需要知道什麼？" | "這個 CLAUDE.md 真的幫到 Agent 了嗎？" | "這東西值不值得做？" |
| **首次使用時間** | 30 秒 | 5 分鐘 | 30 分鐘 |

---

## Skills

### 1. session-end — 會話交接標準化執行器

> **「你正在結束一個改變了項目狀態的會話。下一個會話必須知道什麼？」**

標準化會話交接執行器（基於 AI 協作框架 §9.3）。防止跨會話上下文丟失。

**會話開始檢查清單（展示 4/7 項）：**
- 驗證 CLAUDE.md + MEMORY.md 已加載且為最新
- 檢查記憶陳舊度（>30 天 → 標記待審查）
- 加載 project_status.md 並確認當前階段
- 確認環境（Python 版本、工作目錄、數據文件可達性）

**會話結束檢查清單（5 個模塊）：**
- 更新 project_status.md（固定 4 段結構）
- 同步記憶文件（陳舊 ≠ 不準確——交叉檢查語義內容，不只是時間戳）
- 捕獲跨任務教訓 → `memory/*.md`
- 標記 Retrospect 候選（方法論/流程/工具體系發現）
- 寫標準化 Next Steps（含優先級 + 依賴關係）

**觸發條件：** 產生或改變了項目狀態的會話結束時。快問快答（<5 輪，無文件變更）不用。

**文件：** `SKILL.md` · [reference/](../session-end/reference/) · [scripts/](../session-end/scripts/) · [templates/](../session-end/templates/)

---

### 2. write-claude-md — 項目級 CLAUDE.md 編寫/優化執行器

> **「對每一行問：刪掉它 → Agent 會不會犯錯？不會就砍。」**

五步協議——創建或審計項目級 CLAUDE.md 文件。不是模板填空——是結構化審計，問每一行是否真的約束了 Agent 行為。

**步驟 0 + 五步協議：**

| 步驟 | 內容 | 核心問題 |
|:--:|------|---------------|
| 0 | 上下文收集 | 項目已經告訴了我們什麼？ |
| 1 | 脆弱性測試 | 刪掉這行 → Agent 會不會搞砸？ |
| 2 | 五缺檢查 | 命令、規範、約束、環境、避坑都覆蓋了嗎？ |
| 3 | 五濫檢查 | 是否包含了可推導信息、通用建議、易變數據、文件目錄、空泛建議？ |
| 4 | 實證規則 | 白名單指針化、術語顯式定義、不維護「最後更新」日期 |
| 5 | 多後端驗證 | （重要項目）同 prompt → ≥2 個不同後端 → 收斂/衝突解決 |

**生命週期感知：** 活躍/維護/CLOSED-凍結項目使用不同權重。CLOSED 項目優先記錄避坑和重啟動指令，而非活躍開發命令。

**文件：** `SKILL.md` · [reference/](../write-claude-md/reference/) · [templates/](../write-claude-md/templates/)

---

### 3. kill-test-first — 事前否決 + 預登記

> **「最貴的錯誤不在執行——在那些沒人問過'值不值得做'就開始的事情。」**

預登記決策審計——面向新研究方向、量化策略或論文選題。在動工前強制回答「這東西值不值得做？」。

**雙門協議：**

```
門1：事前否決（步驟 0→8）
  可證偽命題 → 先驗對標 → 最強反方 →
  死亡判據（在看到結果前制定）→ 最便宜證偽 + 強基線 →
  三態裁決：GO / STOP / REDESIGN

門2：預登記凍結（僅當 GO 時）
  凍結協議/指標/判據 → 跑確認性測試 →
  禁止看到數據後挪目標
```

**量化策略紅線（6 條不可妥協檢查）：**
1. 無洩漏/前視偏差
2. 最強基線比較（不能是稻草人）
3. 清晰的樣本外定義
4. 噪聲地板/顯著性檢驗
5. 交易成本/容量限制
6. 多重比較校正

**文件：** `SKILL.md` · [reference/](../kill-test-first/reference/) · [EXAMPLES.md](../kill-test-first/EXAMPLES.md)

---

## 設計思路

- **路由器模式**：SKILL.md 僅含核心流程 + Quick Reference 路由表，詳細參考件外置到 `reference/` 目錄，Agent 按需讀取而非全量加載，控制常駐 Token 消耗
- **漸進式披露**：Skill 主體只暴露入口和觸發條件，具體步驟、模板、腳本由 Agent 根據上下文自行路由加載
- **允許工具白名單**：每個 Skill 聲明 `allowed-tools`，防止 Agent 在 Skill 上下文中越權操作

## 安裝

### 前置要求

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)
- `~/.claude/skills/` 目錄（如不存在：`mkdir -p ~/.claude/skills/`）

### 安裝全部三個

```bash
git clone https://github.com/redamancy231-create/claude-skills.git
cp -r claude-skills/session-end ~/.claude/skills/
cp -r claude-skills/write-claude-md ~/.claude/skills/
cp -r claude-skills/kill-test-first ~/.claude/skills/
```

### 只裝一個

```bash
git clone https://github.com/redamancy231-create/claude-skills.git
cp -r claude-skills/session-end ~/.claude/skills/   # 選你需要的
```

---

## Skill 關係

```
┌──────────────────────────────────────────────────┐
│                  項目生命週期                      │
│                                                  │
│  kill-test-first          write-claude-md         │
│  ┌─────────────┐         ┌──────────────┐        │
│  │ 值不值得做？  │  GO →   │ 為 Agent      │        │
│  │ GO/STOP/    │────────▶│ 記錄項目      │        │
│  │ REDESIGN    │         └──────┬───────┘        │
│  └─────────────┘                │                 │
│                                  │                 │
│                    session-end   │                 │
│                    ┌─────────────▼───────────┐    │
│                    │ 把會話狀態交接給下一個     │    │
│                    │ 更新 project_status.md   │    │
│                    │ 捕獲教訓                  │    │
│                    │ 標記 Retrospect           │    │
│                    └─────────────────────────┘    │
└──────────────────────────────────────────────────┘
```

| Skill | 關係 |
|-------|------|
| `kill-test-first` → `write-claude-md` | 重大 CLAUDE.md 重寫可選擇先過 kill-test |
| `write-claude-md` → `session-end` | 修改 CLAUDE.md 後，session-end 記錄變更 |
| `session-end` → `write-claude-md` | write-claude-md 讀取 session-end 維護的 `project_status.md` 以檢測項目生命週期 |

---

## 相關項目

| 項目 | 關係 |
|------|------|
| [**AI 協作框架**](https://github.com/redamancy231-create/ai-collaboration-framework) | **方法論上游** — 這些 Skill 從框架 §9.2–§9.3 提取，經 50+ 輪跨模型審查 |
| [**Independent Review Toolkit**](https://github.com/redamancy231-create/independent-review-toolkit) | **審查方法來源** — 集合中每個 Skill 均使用該工具包 SOP 進行獨立驗證 |
| [**Prompt-TDD Methodology**](https://github.com/redamancy231-create/prompt-tdd-methodology) | **同系項目** — kill-test-first 是 prompt-TDD 對照實驗協議的直接應用 |
| [**DOCX Pipeline**](https://github.com/redamancy231-create/docx-pipeline) | **同系項目** — Markdown → 中文 DOCX 管道；在其 3 輪審查過程中使用了 session-end 和 write-claude-md |
| [**ETF Pattern Match — pybind11**](https://github.com/redamancy231-create/etf-pattern-match-pybind11) | **同系項目** — C++20/pybind11 量化策略加速；同樣應用多模型審查閉合 |
| [**M&A Case Study Pipeline**](https://github.com/redamancy231-create/ma-case-study-pipeline) | **同系項目** — 8 階段多模型學術生產流水線，含交叉盲審對照實驗 |
| [**Awesome Skills**](https://github.com/gmh5225/awesome-skills) | **收錄於** — 本 Skill 集合已被 awesome-skills 精選目錄收錄 |

## 許可

CC BY 4.0 — 詳見各 `SKILL.md` frontmatter 中的 per-skill provenance 和驗證狀態。

## 關於

| | |
|---|---|
| **來源** | 提煉自 [AI 協作框架](https://github.com/redamancy231-create/ai-collaboration-framework) §9.2–§9.3 + 50+ 輪跨模型審查 |
| **審查鏈** | 每個 Skill 由 ≥2 個不同 LLM 後端獨立審查，零捲入設計 |
| **維護者** | [@redamancy231-create](https://github.com/redamancy231-create) |

*由 DeepSeek-V4-Pro (via Claude Code CLI) 生成 · 2026-07-10*
