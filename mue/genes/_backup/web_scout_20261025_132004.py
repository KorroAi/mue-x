"""
Gene: web_scout — Search and fetch web content.
This gene handles information gathering from the web.
It can be mutated to add new search engines, improve parsing, or add caching.
"""
import json
import urllib.request
import urllib.parse

def search_web(query: str, max_results: int=3) -> list[dict]:
    """Search the web and return structured results."""
    results = []
    try:
        encoded = urllib.parse.quote(query)
        url = f'https://html.duckduckgo.com/html/?q={encoded}'
        req = urllib.request.Request(url, headers={'User-Agent': 'MUE-Agent/0.1'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='replace')
            for line in html.split('\n'):
                if 'result__snippet' in line and len(results) < max_results:
                    snippet = line.split('>')[-1].split('<')[0].strip()
                    if snippet:
                        try:
                            results.append({'title': '', 'snippet': snippet, 'url': ''})
                        except Exception as e:
                            print(f'[EVO] Error: {e}')
    except Exception:
        pass
    return results

def quick_search(query: str) -> str:
    """Fast search returning a text summary."""
    results = search_web(query, max_results=2)
    if not results:
        return f'[No web results for: {query}]'
    return '\n'.join((r['snippet'][:200] for r in results))