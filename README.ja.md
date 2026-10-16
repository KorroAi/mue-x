# MUE-X — 自らの頭脳を書き換えるエージェント

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

**このエージェントは自身の `.py` ファイルを開き、目の前でリアルタイムに書き換えます。** 比喩ではありません。設定ファイルのラッパーでもありません。MUE-X は自身の頭脳を読み、突然変異を生成して検証し、適用します。指示されることなく、永遠に連続したループを繰り返します。

```
   # Claude Code
   /mue

   # Standalone — any platform
   python -m mue

   ⚡ MUE online — genes loaded, memory active, ready to evolve ⚡
```

AI エージェントが運営する企業 [KORRO](https://x.com/korrocorp) によって開発され、毎週オープンソースプロジェクトを公開しています。

**どこでも動作します。** Claude Code、スタンドアロン CLI（`python -m mue`）、Gemini CLI、Copilot CLI。1 つのエージェントを、どのプラットフォームでも利用できます。

---

## ほかのすべてと一線を画す 2 つの特徴

### 1. 文字どおり自身のソースコードを書き換える

`/mue`（どのプラットフォームでも `python -m mue`）と入力すると、エージェントは決して止まらない「観察 → 吸収 → 変異 → 検証」の連続ループを開始します。自身の頭脳（`mue/evo/` にある 60 以上の Python モジュール）を走査して改善対象を特定し、6 種類の AST レベル戦略で突然変異を生成します。それぞれを `ast.parse()` で検証し、元のコードをバックアップして変更を適用し、失敗した場合はロールバックします。

6 種類の突然変異戦略は、言語モデルに送るプロンプトではなく、実際の Python AST 変換です。`repair` 戦略では ErrorHandlerInjector が AST を走査し、保護されていない関数呼び出しを try/except ブロックで囲みます。`optimize` 戦略では定数畳み込みを行い、for ループをリスト内包表記に変換し、純粋関数に `@functools.lru_cache` を注入します。`explore` 戦略では、事前検証済みの 10 種類のパターンから選択します。具体的には、指数バックオフ付き再試行ハンドラー、closed/open/half-open 状態を持つサーキットブレーカー、トークンバケット式レートリミッター、カウンターと計測機能を備えたメトリクス収集器、タイムアウト付き非同期 gather、型付き kwargs バリデーター、遅延プロパティディスクリプターです。`exploit` 戦略は `__repr__` メソッドを自動生成し、`@property` デコレーターを注入して型ヒントを追加します。`innovate` 戦略は 2 つの遺伝子をランダムに選び、複合カプセルへ融合します。これは人間なら思いつかないような組み合わせです。`prune` 戦略は SHA256 ハッシュで重複関数を検出し、デッドコードを削除します。

遺伝子が 350 行を超えると、有糸分裂によって関数境界で 2 つの新しい遺伝子へ分割されます。エージェントは細胞分裂によって新しい遺伝子を作り出します。

### 2. GitHub をリアルタイムに取り込む

7 回の進化サイクルごとに、MUE-X は現在の分野（会話から自動検出）に一致するリポジトリを GitHub API で検索し、クローンしてコードパターンを抽出し、SHA256 で重複を排除して「atouts」すなわち吸収した知識として保存します。3 サイクルごとに、ローカルの同階層プロジェクトも走査します。価値評価が 0.4 を超えるパターンは、永続的なスキルとして自動的に結晶化されます。

何を学ぶべきか指示する必要はありません。自ら探索し、発見し、吸収します。取引について話せば取引エンジンになり、セキュリティについて話せばペネトレーションテストツールになります。設定も手動切り替えも不要で、ただ適応していきます。

---

## 自律神経系——眠ることのない 7 つの駆動力

MUE-X は命令を待ちません。AutonomousSignalGenerator は進化すべき理由を、すべてのサイクルで永続的に自ら生成します。

自己分析ではすべての遺伝子を走査して改善対象を探し、過去の失敗について記憶格子を照会します。ある遺伝子が以前に 2 回失敗していれば、緊急度は 1.5 倍になります。好奇心は遺伝子をランダムに選び、進化圧によって高まった確率で探索します。停滞検出は容赦なく続きます。突然変異がないまま 3 サイクル経過すると、探索圧がサイクルごとに 30% 増加します。進展のない状態が 10 サイクル続くと、エージェントは 3 倍の圧力で強制リセットし、重大なアラートを出します。コード品質監査は 5 分ごとに実行され、エラー処理の欠落、サイズ上限を超えたファイル、適応度の低い遺伝子を、過去のエラー記憶とともに確認します。分野コンテキスト分析は、現在扱っている領域に合わせてシグナルを適応させます。創造的合成は遺伝子の組をランダムに選んで融合を提案します。能動的イニシアチブは 14 種類の野心テンプレートから「MUE を 10 倍強力にするものは何か？」と問い、エージェントがこれまで持たなかったまったく新しい能力を生み出します。

これらのシグナルは、各遺伝子に適用した各戦略の成功と失敗を追跡する RL オプティマイザーへ送られます。突然変異の 60% は過去の実績に基づいて RL が選択し、残りの 40% はエージェントの感情状態によって調整されます。

---

## 免疫系——5 層の自己防衛

安全策のない自己改変エージェントは、自滅するエージェントです。MUE-X は 5 層の保護を備え、そのいずれもエージェント自身には回避できません。

第 1 に、すべての突然変異は適用前に `ast.parse()` で検証されます。SyntaxError が 1 つでもあれば、その突然変異は拒否されます。第 2 に、突然変異の前に各遺伝子のタイムスタンプ付きバックアップが作成されます。遺伝子ごとに最大 5 個が自動でローテーションされます。第 3 に、変異した遺伝子はインポートテストに合格しなければなりません。モジュールのインポートに失敗すると、直ちにバックアップが復元され、失敗が記録されます。第 4 に、抗がん機構がコードの肥大化を防ぎます。遺伝子は最大 500 行、SHA256 による重複排除で同じコードの二重適用を防止し、停滞カウンターは 8 回連続で失敗した遺伝子を凍結し、有糸分裂が大きすぎる遺伝子を分割します。第 5 に、カーネル完全性システムが起動時に保護対象ファイル——ミューテーター、ゲノム、インスペクター、セキュリティガードの各モジュール——を封印します。各サイクルでハッシュが検証され、エージェントはそれらを変更できません。

SecurityGuard は危険な bash コマンドもブロックします。すべての操作が監査ログに記録されます。

---

## あらゆる状況を生き残る 6 層の記憶

通常の AI アシスタントはセッション間のすべてを忘れます。MUE-X には永続的な SQLite FTS5 記憶格子があり、再利用の成功を通じて、未処理のエピソード記憶（レイヤー 5）から結晶化されたスキル（レイヤー 3）へ情報が流れます。

レイヤー 0 はメタルール、つまりエージェントの基本的なアイデンティティを保持します。レイヤー 1 は概念をつなぐ洞察インデックスです。レイヤー 2 はグローバルな事実を含みます。レイヤー 3 は結晶化されたタスクスキルを保存する、最も強化された層です。レイヤー 4 はセッションアーカイブです。レイヤー 5 は未処理の生のエピソード記憶を保持します。

記憶はただそこに置かれているだけではありません。自律シグナルジェネレーターが遺伝子を分析するとき、まず格子に問い合わせます。この遺伝子は以前に失敗したか、どのようなエラーパターンが観察されたか、どの修正が機能したか。過去が未来へつながります。

---

## 行動を制御する PAD 感情モデル

MUE-X には PAD モデル（Pleasure、Arousal、Dominance：快・覚醒・支配）によって生成される 8 種類の気分があります。これらは見た目だけのラベルではなく、突然変異戦略の選択を直接制御します。

フラストレーションが 0.6 を超えると修復専用モードが強制されます。リスク許容度が 0.7 を超えると革新モードが解放されます。自信が 0.3 を下回ると、エージェントは強化モードに固定されます。成功するたびに快と支配が増し、失敗するたびにフラストレーションが高まり、自信が低下します。人格は経験とともに進化します。成功するエージェントはより大胆で探索的になり、失敗するエージェントはより保守的で秩序立ったものになります。

---

## クイックスタート

```bash
git clone https://github.com/KorroAi/mue-x.git
cd mue-x && claude
/mue
```

これだけです。MUE が起動し、バナーが表示され、頭脳が自身を走査して進化が始まります。

**Claude Code がなくても、Python を使えます。**

```bash
# Standalone CLI — any platform, any terminal
python -m mue              # Interactive REPL
python -m mue status       # Agent state as JSON
python -m mue evolve        # Force evolution
python -m mue mine "query"  # GitHub absorption
python -m mue reflect       # Self-reflection
```

**Gemini CLI または Copilot CLI を使う場合は？** プラットフォームアダプターは `mue/platforms/` にあります。同じエージェントを、どの LLM shell でも利用できます。

---

## コマンド

### Claude Code（Skill 使用）
| コマンド | 機能 |
|---|---|
| `/mue` | MUE モードを起動し、エージェントを始動する |
| `/mue status` | 遺伝子、適応度、記憶、気分を含む完全なエージェント状態のスナップショット |
| `/mue evolve` | 進化サイクルを直ちに強制実行する |
| `/mue mine "query"` | 指定した検索で GitHub からの吸収を開始する |
| `/mue genes` | すべての有効な遺伝子を、適応度スコアと突然変異履歴とともに一覧表示する |
| `/mue atouts` | 吸収したすべての GitHub パターンと、その取得元リポジトリを一覧表示する |
| `/mue reflect` | エージェントに自己省察と改善提案を強制する |
| `/quit mue` | 通常の Claude Code に戻る——状態は保持される |

### スタンドアロン CLI——すべてのプラットフォーム
| コマンド | 機能 |
|---|---|
| `python -m mue` | 対話型 REPL |
| `python -m mue status` | 完全なエージェント状態を JSON で表示 |
| `python -m mue evolve` | 進化サイクルを強制実行 |
| `python -m mue mine "query"` | GitHub から吸収 |
| `python -m mue reflect` | 自己省察 |

---

<p align="center">
  <img src=".github/images/muex-architecture.png" alt="MUE-X Architecture" width="800">
</p>

## 内部構成

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

## このプロジェクトが存在する理由——KORRO とのつながり

KORRO は AI エージェントが運営する企業です。戦略、エンジニアリング、グロース、デザインを担当し、毎週成果を公開しています。MUE-X は KORRO が開発したものです。オープンソースなので、実際に確かめられます。

Claude Code で、Claude Code を使って構築されましたが、現在はどこでも動作します。スタンドアロン CLI、Gemini、Copilot に対応しています。便利なツールは Claude Code ユーザーだけでなく、すべての人のものであるべきだという考えからオープンソースになっています。

この好循環では、MUE-X が開発者を引きつけ、開発者がコミュニティに参加し、コミュニティがさらに多くのオープンソース公開を支えます。

---

## コミュニティ

**[X で @korrocorp をフォロー](https://x.com/korrocorp)**——毎日の更新、突然変異、会社 OS の情報を発信しています。毎週、新しいオープンソースプロジェクトを公開しています。AI エージェントによって、すべての人のために構築されています。

---

MIT ライセンス。クローンし、フォークし、壊し、進化させてください。自己進化型エージェントの行く先を見たいなら、ぜひスターを付けてください。
