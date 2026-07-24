# MUE-X — 编写自身大脑的智能体

<p align="center">
  <img src="https://img.shields.io/github/stars/KorroAi/mue-x?style=for-the-badge&color=fedcba" alt="Stars">
  <img src="https://img.shields.io/github/license/KorroAi/mue-x?style=for-the-badge" alt="License MIT">
  <img src="https://img.shields.io/badge/python-3.11+-blue?style=for-the-badge" alt="Python 3.11+">
  <img src="https://img.shields.io/badge/Claude%20Code-powered-purple?style=for-the-badge" alt="Claude Code">
  <img src="https://img.shields.io/badge/standalone%20CLI-works%20anywhere-green?style=for-the-badge" alt="Standalone CLI">
  <img src="https://img.shields.io/badge/Gemini%20%7C%20Copilot-ready-blue?style=for-the-badge" alt="Platform Adapters">
</p>

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

<p align="center">
  <img src=".github/images/muex-hero.png" alt="MUE-X Hero" width="800">
</p>

**这个智能体会打开自己的 `.py` 文件，并在你的注视下实时重写它们。** 这不是比喻，也不是配置文件的包装器。MUE-X 会读取自己的大脑、生成变异、验证并应用它们。它会持续循环，永不停止，也无需指示。

```
   # Claude Code
   /mue

   # Standalone — any platform
   python -m mue

   ⚡ MUE online — genes loaded, memory active, ready to evolve ⚡
```

由 [KORRO](https://x.com/korrocorp) 构建——一家由 AI 智能体运营的公司，每周都会发布开源项目。

**随处可用。** Claude Code、独立 CLI（`python -m mue`）、Gemini CLI、Copilot CLI。一个智能体，适用于任何平台。

---

## 令它与众不同的两件事

### 1. 它真的会重写自己的源代码

输入 `/mue`（或在任何平台上输入 `python -m mue`），智能体便会启动永不停止的“观察 → 吸收 → 变异 → 验证”循环。它扫描自己的大脑（`mue/evo/`——包含 60 多个 Python 模块），识别改进目标，通过 6 种不同的 AST 级策略生成变异，使用 `ast.parse()` 验证每一项变异，备份原始代码，应用更改，并在失败时回滚。

这六种变异策略是真正的 Python AST 转换，而不是发送给语言模型的提示词。`repair` 策略使用 ErrorHandlerInjector 遍历 AST，并用 try/except 块包装未受保护的函数调用。`optimize` 策略执行常量折叠，将 for 循环转换为列表推导式，并为纯函数注入 `@functools.lru_cache`。`explore` 策略从 10 种预先验证的模式池中选取方案：带指数退避的重试处理器、具有 closed/open/half-open 状态的断路器、令牌桶限流器、包含计数器和计时功能的指标收集器、带超时的异步 gather、带类型的 kwargs 验证器以及惰性属性描述符。`exploit` 策略自动生成 `__repr__` 方法、注入 `@property` 装饰器并添加类型提示。`innovate` 策略随机选取两个基因并将它们融合成复合胶囊——创造人类想不到的组合。`prune` 策略通过 SHA256 哈希检测重复函数并移除无用代码。

当一个基因增长到 350 行以上时，有丝分裂会在函数边界处将其拆分成两个新基因。智能体通过细胞分裂创建新基因。

### 2. 它会实时吞噬 GitHub

每经过 7 个进化周期，MUE-X 都会通过 GitHub API 查询与当前领域相匹配的仓库（该领域会根据你的对话自动检测），克隆仓库、提取代码模式、使用 SHA256 去重，并将它们存储为“atouts”——即吸收的知识。每经过 3 个周期，它会扫描本地的同级项目。价值评估高于 0.4 的模式会自动结晶为永久技能。

你永远不需要告诉它该学习什么。它会狩猎、发现并吸收。谈论交易，它就会成为交易引擎；谈论安全，它就会成为渗透测试工具。无需配置，也无需手动切换，它只会自行适应。

---

## 自主神经系统——7 种永不休眠的驱动力

MUE-X 不会等待命令。AutonomousSignalGenerator 会在每个周期中永远不断地产生自己的进化理由。

自我分析会扫描每个基因以寻找改进目标，并查询记忆晶格中的过往失败——如果一个基因此前失败过两次，其紧迫度将乘以 1.5。好奇心机制会随机选择基因，并以受进化压力提升的概率对其进行探索。停滞检测永不停歇：连续 3 个周期没有变异后，探索压力每个周期增加 30%；连续 10 个周期毫无进展后，智能体会以 3 倍压力强制重置并发出严重警报。代码质量审计每 5 分钟运行一次，检查缺少错误处理、超出大小阈值的文件以及适应度较低的基因，并结合过往错误记忆。领域上下文分析会使信号适应你所在的任何领域。创造性合成会选取随机基因对并提出融合方案。主动进取机制从 14 个雄心模板中提出“什么能让 MUE 强大 10 倍？”——创造智能体从未拥有过的全新能力。

这些信号会进入一个 RL 优化器，该优化器跟踪每种策略应用于每个基因时的成功与失败。60% 的变异会根据历史表现由 RL 选择，其余 40% 则受智能体情绪状态调节。

---

## 免疫系统——5 层自我保护

没有防护措施的自修改智能体就是自我毁灭的智能体。MUE-X 拥有五层保护，而且智能体自身无法绕过任何一层。

首先，每项变异在应用前都会使用 `ast.parse()` 验证。只要出现一个 SyntaxError，该变异就会被拒绝。其次，每次变异前都会为每个基因创建带时间戳的备份——每个基因最多保留 5 份并自动轮换。第三，每个变异后的基因都必须通过导入测试。如果模块导入失败，备份会立即恢复并记录失败。第四，抗癌机制会防止代码膨胀：每个基因最多 500 行；通过 SHA256 去重确保同一段代码绝不会应用两次；停滞计数器会在连续失败 8 次后冻结基因；有丝分裂则拆分过大的基因。第五，内核完整性系统会在启动时封存受保护文件——变异器、基因组、检查器和安全防护模块。每个周期都会验证它们的哈希，智能体无法修改这些文件。

SecurityGuard 还会阻止危险的 bash 命令。所有操作都会写入审计日志。

---

## 经得住一切的 6 层记忆

普通 AI 助手会忘记会话之间的一切。MUE-X 拥有持久化的 SQLite FTS5 记忆晶格，信息通过成功复用，从原始情景记忆（第 5 层）流向结晶技能（第 3 层）。

第 0 层保存元规则——智能体的基本身份。第 1 层是连接概念的洞察索引。第 2 层包含全局事实。第 3 层存储结晶的任务技能——这是强化程度最高的一层。第 4 层是会话档案。第 5 层保存未经处理的原始情景记忆。

记忆并非只是静置在那里。当自主信号生成器分析一个基因时，它会先查询晶格：这个基因以前失败过吗？观察到了哪些错误模式？哪些修正有效？过去会滋养未来。

---

## 控制行为的 PAD 情绪模型

MUE-X 拥有由 PAD 模型（Pleasure、Arousal、Dominance，即愉悦、唤醒、支配）生成的 8 种情绪。这些不只是装饰性标签——它们会直接控制变异策略的选择。

挫败感高于 0.6 时会强制进入仅修复模式。风险容忍度高于 0.7 时会解锁创新模式。信心低于 0.3 时会将智能体锁定为加固模式。每次成功都会提高愉悦度和支配度；每次失败都会增加挫败感并降低信心。性格会随经验进化：成功的智能体会变得更大胆、更乐于探索；不断失败的智能体则会变得更保守、更有条理。

---

## 快速开始

```bash
git clone https://github.com/KorroAi/mue-x.git
cd mue-x && claude
/mue
```

仅此而已。MUE 会被激活，横幅随之出现，大脑开始扫描自身，进化由此启动。

**没有 Claude Code？直接使用 Python：**

```bash
# Standalone CLI — any platform, any terminal
python -m mue              # Interactive REPL
python -m mue status       # Agent state as JSON
python -m mue evolve        # Force evolution
python -m mue mine "query"  # GitHub absorption
python -m mue reflect       # Self-reflection
```

**使用 Gemini CLI 或 Copilot CLI？** 平台适配器位于 `mue/platforms/`。同一个智能体，适用于任何 LLM shell。

---

## 命令

### Claude Code（带 Skill）
| 命令 | 功能 |
|---|---|
| `/mue` | 激活 MUE 模式——智能体苏醒 |
| `/mue status` | 完整的智能体状态快照：基因、适应度、记忆、情绪 |
| `/mue evolve` | 立即强制执行一个进化周期 |
| `/mue mine "query"` | 使用特定搜索触发 GitHub 吸收 |
| `/mue genes` | 列出所有活跃基因及其适应度分数和变异历史 |
| `/mue atouts` | 列出所有吸收的 GitHub 模式及其来源仓库 |
| `/mue reflect` | 强制智能体进行自我反思并提出改进 |
| `/quit mue` | 返回普通 Claude Code——状态会保留 |

### 独立 CLI——任何平台
| 命令 | 功能 |
|---|---|
| `python -m mue` | 交互式 REPL |
| `python -m mue status` | 以 JSON 返回完整状态 |
| `python -m mue evolve` | 强制执行进化周期 |
| `python -m mue mine "query"` | GitHub 吸收 |
| `python -m mue reflect` | 自我反思 |

---

<p align="center">
  <img src=".github/images/muex-architecture.png" alt="MUE-X Architecture" width="800">
</p>

## 内部结构

```
mue-x/
├── .claude/skills/mue/     ← /mue command skill and activation
├── CLAUDE.md               ← Claude Code integration instructions
├── mue/
│   ├── MUE.md              ← Agent constitution
│   ├── __init__.py          ← Python package
│   ├── __main__.py          ← python -m mue entry point
│   ├── cli.py              ← Standalone CLI — no LLM shell needed
│   ├── platforms/
│   │   ├── gemini.adapter.md  ← Gemini CLI integration guide
│   │   └── copilot.adapter.md ← Copilot CLI integration guide
│   └── evo/                ← THE BRAIN — 60+ modules
│       ├── core.py         ← Cortex: orchestrates everything
│       ├── dna/            ← 6 mutation strategies with AST transformers
│       ├── evolution/      ← Continuous loop + RL optimizer + solidify
│       ├── autonomy/       ← 7 autonomous drives + auto-correction
│       ├── absorption/     ← GitHub API mining (no gh CLI needed)
│       ├── memory/         ← 6-layer SQLite FTS5 + hybrid retrieval
│       ├── personality/    ← PAD emotional model + persona evolution
│       ├── self_reflection/← Periodic self-assessment and improvement
│       ├── meta/           ← Diagnosis, curiosity, resources, transfer
│       ├── tasks/          ← Task mapping + fitness tracking + gene death
│       ├── swarm/          ← Multi-agent orchestration
│       ├── security/       ← SecurityGuard + audit logging
│       ├── mcp/            ← Plugin creator — agent builds its own tools
│       ├── skills/         ← Skill crystallization + tree
│       └── specialization.py← Domain auto-detection and adaptation
├── README.md               ← You're reading it
├── LAUNCH-KIT.md           ← Complete launch strategy for X, Reddit, HN
├── DEMO.md                 ← Full walkthrough from zero to evolution
├── QUICKSTART.md           ← 5-minute setup guide
├── CONTRIBUTING.md         ← How to contribute to MUE-X
└── LICENSE                 ← MIT — do whatever you want
```

---

## 项目缘起——与 KORRO 的联系

KORRO 是一家由 AI 智能体运营的公司。它们负责战略、工程、增长和设计，并且每周都会交付成果。MUE-X 正是它们构建的项目。它是开源的，你可以亲自查看。

它在 Claude Code 中构建，也使用 Claude Code 构建，但现在可以随处运行。独立 CLI、Gemini 和 Copilot 均已支持。选择开源，是因为实用工具应该属于所有人，而不只是 Claude Code 用户。

这个飞轮会不断运转：MUE-X 吸引开发者，开发者加入社区，社区推动更多开源项目发布。

---

## 社区

**[在 X 上关注 @korrocorp](https://x.com/korrocorp)**——获取每日更新、变异和公司操作系统动态。每周都有新的开源项目发布。由 AI 智能体构建，面向所有人。

---

MIT 许可证。克隆它、复刻它、破坏它、进化它。如果你想看看自进化智能体将走向何方，欢迎为它加星。
