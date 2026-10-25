"""MUE-X REST API — Control and monitor the agent from anywhere.

Usage:
    pip install fastapi uvicorn
    python -m mue serve
"""

import json
from pathlib import Path


def _get_fastapi():
    """Lazy import FastAPI — only needed for serve mode."""
    try:
        from fastapi import FastAPI, Query
        return FastAPI, Query
    except ImportError:
        raise ImportError(
            "FastAPI is required for API mode. Install with: pip install fastapi uvicorn"
        )


def _agent():
    from mue.evo.core import MueAgent
    work_dir = Path(__file__).resolve().parent
    return MueAgent(str(work_dir))


def create_app():
    """Create the FastAPI app (lazy — only when serve is used)."""
    FastAPI, Query = _get_fastapi()

    app = FastAPI(title="MUE-X API", version="1.0.0", docs_url="/api/docs")

    @app.get("/api/status")
    def get_status():
        a = _agent()
        return a.state

    @app.post("/api/evolve")
    def trigger_evolve():
        a = _agent()
        result = a.chat("/mue evolve")
        return {"ok": True, "response": result.get("text", "")}

    @app.post("/api/mine")
    def trigger_mine(query: str = Query("AI agent patterns")):
        a = _agent()
        result = a._handle_mine_command(query)
        return {"ok": True, "result": result}

    @app.post("/api/reflect")
    def trigger_reflect():
        a = _agent()
        result = a._handle_reflect_command()
        return {"ok": True, "response": result.get("text", "")}

    @app.get("/api/genes")
    def list_genes():
        a = _agent()
        return {"genes": a.state.get("genes", [])}

    return app


# Module-level app for uvicorn (uvicorn mue.api:app)
# Created lazily when first accessed
_app = None

def __getattr__(name):
    global _app
    if name == "app":
        if _app is None:
            _app = create_app()
        return _app
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
