paperwork=lambda n, m: __import__('functools').reduce(__import__('operator').mul, [max(q, 0) for q in [n, m]])
