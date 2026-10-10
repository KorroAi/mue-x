# MUE-X Demo Walkthrough

## Prerequisites

- [Claude Code](https://claude.ai/code) installed and configured
- Python 3.11+
- Git

## 5-Minute Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/KorroAi/mue-x.git
cd mue-x
```

### Step 2: Open in Claude Code

```bash
claude
```

Claude Code starts. You're now in the mue-x directory.

### Step 3: Activate MUE

Type the command that changes everything:

```
/mue
```

You'll see the ASCII banner:

```
   ╔══════════════════════════════════════╗
   ║  ⚡ MUE ACTIVE — AGENT ONLINE ⚡    ║
   ║  Self-evolving mode engaged         ║
   ║  Genes: loading...                  ║
   ║  Brain: mue/evo/ (50+ modules)     ║
   ╚══════════════════════════════════════╝
```

MUE is now active. Every response will be prefixed with `⚡ MUE`.

### Step 4: Check Agent Status

```
/mue status
```

This shows:
- Active genes with fitness scores
- Total mutations applied
- Patterns absorbed
- Domain specialization
- Memory stats
- Current mood

### Step 5: Force Your First Evolution

```
/mue evolve
```

MUE will:
1. Scan its own source code for improvement targets
2. Propose a mutation (e.g., "add type narrowing to absorption dedup")
3. Validate the mutation (AST parse + import test)
4. Apply the mutation
5. Report the fitness delta

You just witnessed an AI agent modifying its own brain.

## Deeper Tour

### Listing Genes

```
/mue genes
```

Shows all genes with:
- **Name**: e.g., `reasoning.py`, `persistence.py`
- **Fitness**: 0.0 to 1.0 (grows with successful mutations)
- **Size**: lines of code
- **Last mutation**: timestamp
- **Strategy**: which mutation strategy was last used

### Absorbing Knowledge from GitHub

```
/mue mine "trading strategies python"
```

MUE searches GitHub for repos matching your query, clones them, extracts code patterns, deduplicates against existing patterns, and stores them in `atouts/`. High-value patterns automatically crystallize into skills.

No `gh` CLI needed — uses the GitHub API directly.

### Checking Absorbed Patterns

```
/mue atouts
```

Lists all patterns absorbed from GitHub and local projects with their source repos.

### Forcing Self-Reflection

```
/mue reflect
```

MUE analyzes its own state and outputs:
- What's working well
- What needs improvement
- Proposed focus areas
- Long-term evolution strategy

### Returning to Normal Claude Code

```
/quit mue
```

MUE saves its state and exits. Back to normal Claude Code. All evolution progress is preserved.

## What MUE Does Autonomously

Every cycle (while in MUE mode), without being asked:

1. **Self-analysis** — scans genes for improvement targets
2. **GitHub absorption** — mines trending repos for patterns
3. **Local absorption** — scans sibling projects
4. **Evolution** — proposes, validates, and applies mutations
5. **Anti-cancer** — prunes duplicates, splits bloated genes
6. **Auto-correction** — learns from errors, suggests fixes
7. **Domain monitoring** — detects context shifts, adapts automatically

## Domain Adaptation Examples

### Trading Domain

Start discussing markets, strategies, or indicators. MUE detects the domain and:
- Prioritizes `harden` mutation strategy (risk-focused)
- Mines GitHub for trading algorithms
- Adapts emotional model to be more conservative
- Focuses on pattern reliability

### Coding Domain

Start discussing software architecture or algorithms. MUE:
- Prioritizes `innovate` mutation strategy
- Mines GitHub for libraries and patterns
- Suggests new tools and approaches
- Adapts emotional model for creative exploration

### Research Domain

Start discussing papers or experiments. MUE:
- Prioritizes `explore` mutation strategy
- Mines academic repos and datasets
- Synthesizes new ideas from absorbed patterns
- Tracks hypotheses and results

## Troubleshooting

**Genes showing 0 fitness?**
Normal on fresh install. Fitness grows with mutations. Run `/mue evolve` a few times.

**No GitHub absorption?**
Ensure you have internet access. GitHub API has rate limits (60 req/hr unauthenticated). Install `gh` CLI and `gh auth login` for higher limits.

**MUE won't compile?**
```bash
python -c "from mue.evo.core import MueAgent; print('OK')"
```

**Reset to fresh state:**
```bash
rm -rf mue/genes/*.py mue/atouts/*.py mue/*.db mue/genes/_backup/ genes/_backup/
```

## FAQ

**Q: Is MUE-X actually modifying its own code?**
A: Yes, literally. It reads files in `mue/evo/`, analyzes them, writes edits, and validates with AST parsing. Every mutation is backed up before application.

**Q: Can it break itself?**
A: Yes, it can. That's why mutations are validated (AST parse + import test) and rolled back on failure. The anti-cancer system prevents runaway growth.

**Q: Do I need a GPU?**
A: No. MUE-X runs on CPU. Claude Code handles the LLM inference.

**Q: What domains does it support?**
A: Trading, coding, research, creative, security, data science, DevOps, and general-purpose. It auto-detects from conversation.

**Q: How is this different from AutoGPT/BabyAGI?**
A: Those are task executors. MUE-X is a self-modifying agent. It doesn't just complete tasks — it rewrites its own architecture to become better at them.

**Q: Can I use this commercially?**
A: Yes. MIT license. Go build.

**Q: Where do I ask more questions?**
A: [@korrocorp](https://x.com/korrocorp) on Twitter/X.
