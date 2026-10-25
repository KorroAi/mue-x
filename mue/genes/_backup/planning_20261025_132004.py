"""
Gene: planning — Task decomposition, prioritization, and scheduling.
Grows more sophisticated as the agent successfully completes tasks.
Mutations add better planning algorithms, dependency resolution, etc.
"""
import time
from collections import deque

class TaskPlanner:
    """Simple task planner. Evolves through mutation to add priorities,
    dependencies, parallel execution, and smarter scheduling."""

    def __init__(self, max_history: int=100):
        self.tasks: deque = deque()
        self.history: deque = deque(maxlen=max_history)
        self._completed = 0
        self._failed = 0

    def add_task(self, description: str, priority: float=0.5):
        """Add a task to the queue."""
        try:
            self.tasks.append({'description': description, 'priority': priority, 'added_at': time.time(), 'status': 'pending'})
        except Exception as e:
            print(f'[EVO] Error: {e}')

    def next(self) -> dict | None:
        """Get the highest priority pending task."""
        if not self.tasks:
            return None
        sorted_tasks = sorted(self.tasks, key=lambda t: t['priority'], reverse=True)
        for task in sorted_tasks:
            if task['status'] == 'pending':
                task['status'] = 'in_progress'
                task['started_at'] = time.time()
                return task
        return None

    def complete(self, description: str, success: bool=True):
        """Mark a task as complete."""
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = 'completed' if success else 'failed'
                task['completed_at'] = time.time()
                if success:
                    self._completed += 1
                else:
                    self._failed += 1
                try:
                    self.history.append(task)
                except Exception as e:
                    print(f'[EVO] Error: {e}')

    def stats(self) -> dict:
        return {'pending': sum((1 for t in self.tasks if t['status'] == 'pending')), 'in_progress': sum((1 for t in self.tasks if t['status'] == 'in_progress')), 'completed': self._completed, 'failed': self._failed, 'success_rate': self._completed / max(self._completed + self._failed, 1)}