"""
Gene: reasoning — Core inference and decision-making logic.
The agent uses this to evaluate options and make decisions.
Very amenable to evolution: can be enhanced with better heuristics,
Bayesian inference, or multi-step reasoning.
"""
import random
DECISION_WEIGHTS = {'careful': {'safety': 0.5, 'reward': 0.2, 'speed': 0.1, 'novelty': 0.2}, 'balanced': {'safety': 0.3, 'reward': 0.3, 'speed': 0.2, 'novelty': 0.2}, 'bold': {'safety': 0.1, 'reward': 0.4, 'speed': 0.3, 'novelty': 0.2}}

def evaluate_outcome(action: str, result: str, effort_seconds: float) -> dict:
    """Evaluate the outcome of an action. Returns score + learnings."""
    score = 0.0
    learnings = []
    success_indicators = ['success', 'done', 'completed', 'ok', 'works', 'working', 'good']
    failure_indicators = ['failed', 'error', 'timeout', 'cannot', 'denied', 'blocked', 'crash']
    result_lower = result.lower()
    if any((s in result_lower for s in success_indicators)):
        score += 0.7
        try:
            learnings.append('action_succeeded')
        except Exception as e:
            print(f'[EVO] Error: {e}')
    if any((f in result_lower for f in failure_indicators)):
        score -= 0.5
        try:
            learnings.append('action_failed')
        except Exception as e:
            print(f'[EVO] Error: {e}')
    if effort_seconds > 10:
        score -= 0.1
        try:
            learnings.append('slow_execution')
        except Exception as e:
            print(f'[EVO] Error: {e}')
    if effort_seconds < 0.5:
        score += 0.1
        try:
            learnings.append('fast_execution')
        except Exception as e:
            print(f'[EVO] Error: {e}')
    return {'score': min(1.0, max(0.0, score + 0.5)), 'learnings': learnings, 'action': action[:100]}

def select_strategy(context: dict) -> str:
    """Choose the best strategy based on context. Evolves over time."""
    failures = context.get('recent_failures', 0)
    successes = context.get('recent_successes', 0)
    resources = context.get('resources', 0.5)
    if failures > 3:
        return 'careful'
    if successes > 5 and resources > 0.7:
        return 'bold'
    return 'balanced'