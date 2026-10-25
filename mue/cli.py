"""MUE-X Standalone CLI — No Claude Code required.

Usage:
    python -m mue              # Interactive REPL
    python -m mue status       # Agent state snapshot
    python -m mue evolve       # Force one evolution cycle
    python -m mue mine "query" # GitHub absorption
    python -m mue reflect      # Self-reflection
    python -m mue serve        # Start API server
"""

import sys
import json
import argparse
from pathlib import Path


def get_agent():
    from mue.evo.core import MueAgent
    work_dir = Path(__file__).resolve().parent
    return MueAgent(str(work_dir))


def cmd_status():
    agent = get_agent()
    state = agent.state
    print(json.dumps(state, indent=2, default=str))


def cmd_evolve():
    agent = get_agent()
    result = agent.chat("/mue evolve")
    print(result.get("text", "Evolution complete"))


def cmd_mine(query: str):
    agent = get_agent()
    result = agent._handle_mine_command(query)
    print(json.dumps(result, indent=2, default=str))


def cmd_reflect():
    agent = get_agent()
    result = agent._handle_reflect_command()
    print(result.get("text", "Reflection complete"))


def cmd_serve(host: str = "127.0.0.1", port: int = 8791):
    try:
        import uvicorn
    except ImportError:
        print("uvicorn is required for API mode.")
        print("Install with: pip install fastapi uvicorn")
        sys.exit(1)
    try:
        from mue.api import create_app
        app = create_app()
    except ImportError as e:
        print(f"FastAPI is required for API mode: {e}")
        print("Install with: pip install fastapi uvicorn")
        sys.exit(1)
    print(f" MUE-X API: http://{host}:{port}")
    print(f" Docs: http://{host}:{port}/api/docs")
    uvicorn.run(app, host=host, port=port, reload=False)


def cmd_interactive():
    agent = get_agent()
    print(" MUE-X Standalone CLI")
    print(" Type /help for commands, /quit to exit")
    print()

    while True:
        try:
            msg = input("mue> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nQuitting. State preserved.")
            break

        if not msg:
            continue
        if msg in ("/quit", "/exit", "/q"):
            print("Quitting. State preserved.")
            break
        if msg == "/help":
            print("Commands: /status, /evolve, /mine <q>, /reflect, /genes, /atouts, /quit")
            continue
        if msg == "/status":
            cmd_status()
            continue
        if msg == "/evolve":
            cmd_evolve()
            continue
        if msg.startswith("/mine"):
            query = msg[6:].strip() or "AI agent patterns"
            cmd_mine(query)
            continue
        if msg == "/reflect":
            cmd_reflect()
            continue
        if msg == "/genes":
            agent = get_agent()
            for g in agent.state.get("genes", []):
                print(f"  {g.get('name', '?')} — fitness: {g.get('fitness', 0):.2f}")
            continue
        if msg == "/atouts":
            agent = get_agent()
            for a in agent.state.get("atouts", []):
                print(f"  {a.get('name', '?')} — {a.get('source', '?')}")
            continue

        result = agent.chat(msg)
        print(result.get("text", "(no response)"))


def main():
    parser = argparse.ArgumentParser(description="MUE-X Self-Evolving Agent")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("status", help="Show agent state")
    sub.add_parser("evolve", help="Force evolution cycle")
    sub.add_parser("reflect", help="Self-reflection")
    sub.add_parser("serve", help="Start API server")
    mine_p = sub.add_parser("mine", help="GitHub absorption")
    mine_p.add_argument("query", nargs="?", default="AI agent patterns")

    args = parser.parse_args()

    if args.command == "status":
        cmd_status()
    elif args.command == "evolve":
        cmd_evolve()
    elif args.command == "mine":
        cmd_mine(args.query)
    elif args.command == "reflect":
        cmd_reflect()
    elif args.command == "serve":
        cmd_serve()
    else:
        cmd_interactive()


if __name__ == "__main__":
    main()
