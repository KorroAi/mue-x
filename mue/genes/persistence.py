"""
Gene: persistence — Data storage, caching, and state management.
Handles saving/loading agent state, caching results, and managing files.
This gene grows as the agent learns to use more storage backends.
"""
import json
import time
from pathlib import Path
from typing import Optional

class StateCache:
    """Simple file-based state cache with TTL. Will be enhanced by mutations."""

    def __init__(self, cache_dir: str='.mue_cache'):
        self.cache_dir = Path(cache_dir)
        try:
            self.cache_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f'[EVO] Error: {e}')
        self._memory: dict[str, dict] = {}

    def set(self, key: str, value, ttl_seconds: Optional[float]=None):
        """Store a value with optional TTL."""
        entry = {'value': value, 'stored_at': time.time(), 'ttl': ttl_seconds}
        self._memory[key] = entry
        cache_file = self.cache_dir / f"{key.replace('/', '_')}.json"
        try:
            cache_file.write_text(json.dumps(entry, indent=2), encoding='utf-8')
        except Exception as e:
            print(f'[EVO] Error: {e}')

    def get(self, key: str):
        """Retrieve a value, handling TTL."""
        entry = self._memory.get(key)
        if not entry:
            cache_file = self.cache_dir / f"{key.replace('/', '_')}.json"
            if cache_file.exists():
                try:
                    entry = json.loads(cache_file.read_text(encoding='utf-8'))
                    self._memory[key] = entry
                except (json.JSONDecodeError, IOError):
                    return None
            else:
                return None
        if entry.get('ttl'):
            age = time.time() - entry['stored_at']
            if age > entry['ttl']:
                return None
        return entry['value']

    def stats(self) -> dict:
        """Cache statistics."""
        valid = sum((1 for _ in self._memory))
        return {'cached_entries': valid, 'cache_dir': str(self.cache_dir)}