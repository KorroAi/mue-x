"""
Gene: communication — Message formatting, protocol handling, and output generation.
The agent's voice. Mutations here change HOW the agent speaks,
what formats it supports, and how it structures responses.
"""
import json
import time
from datetime import datetime, timezone

def format_response(text: str, mood: str='neutral', context: dict=None) -> dict:
    """Format a chat response with metadata."""
    context = context or {}
    return {'text': text, 'mood': mood, 'timestamp': time.time(), 'format_version': 1, 'metadata': {'tokens': len(text.split()), 'has_code': '```' in text}}

def generate_summary(events: list[dict], max_items: int=5) -> str:
    """Summarize a list of events into a readable report."""
    if not events:
        return 'No events to report.'
    lines = []
    for event in events[:max_items]:
        ts = event.get('timestamp', 0)
        if isinstance(ts, (int, float)):
            when = datetime.fromtimestamp(ts, tz=timezone.utc).strftime('%H:%M:%S')
        else:
            when = str(ts)
        desc = event.get('description', str(event))[:120]
        try:
            lines.append(f'[{when}] {desc}')
        except Exception as e:
            print(f'[EVO] Error: {e}')
    return '\n'.join(lines)

def sanitize_output(text: str, max_length: int=2000) -> str:
    """Sanitize agent output for safe display."""
    if len(text) > max_length:
        text = text[:max_length - 3] + '...'
    return text.strip()