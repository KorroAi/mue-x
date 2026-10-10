# Contributing to MUE-X

MUE-X evolves by modifying its own code. You can help too.

## How to Contribute

### 1. Use MUE-X and Report

The best contribution is using it. Every session generates evolution data. Share what your MUE evolved into.

### 2. Submit Mutations

If MUE-X proposes a mutation you think is particularly smart, share it:
- Copy the mutation diff from the session
- Open an issue with label `mutation-share`
- Include: what triggered it, fitness delta, strategy used

### 3. Improve the Brain

PRs to `mue/evo/` are welcome. Before submitting:

- Run `python -c "from mue.evo.core import MueAgent; print('OK')"` to validate
- Ensure no `__pycache__`, `.db`, or `mue_config.json` files are included
- No single file should exceed 800 lines (MUE enforces this)
- Explain the improvement in evolutionary terms: what does this enable MUE to do that it couldn't before?

### 4. Add Absorption Targets

Know a great repo MUE-X should learn from? Add it to absorption targets in the issue tracker.

### 5. Share Your Evolution Stories

Screenshots, fitness graphs, interesting mutations — share them on Twitter with `#MUEX` or in GitHub Discussions.

## Vibe Coder's Guide

This project is built by vibe coders — people who build with AI assistance. If you're a vibe coder too, you're in the right place.

### Principles

- **Ship fast, evolve faster** — get it working, then let MUE improve it
- **The code is alive** — treat `mue/evo/` as a living organism, not a static codebase
- **Trust the anti-cancer** — MUE's safeguards exist for a reason. Don't bypass them.
- **Share the mutations** — what your MUE learns can help all MUEs

## Code Standards

- Max 800 lines per file (enforced by anti-cancer)
- Type hints preferred on public methods
- Docstrings on new public methods
- Run brain integrity: `python -c "from mue.evo.core import MueAgent; print('OK')"`

## Development Setup

```bash
git clone https://github.com/KorroAi/mue-x.git
cd mue-x

# Validate brain integrity
python -c "from mue.evo.core import MueAgent; print('OK')"

# Open in Claude Code
claude
/mue
```

## Issue Labels

| Label | Purpose |
|-------|---------|
| `mutation-share` | Share an interesting mutation your MUE generated |
| `bug` | Something is broken |
| `enhancement` | Feature request or improvement idea |
| `mutation-idea` | Suggest a new mutation strategy |
| `domain-request` | Request support for a new domain |
| `good-first-issue` | Good for new contributors |

## Questions?

Tweet [@korrocorp](https://x.com/korrocorp) or open a GitHub Discussion.
