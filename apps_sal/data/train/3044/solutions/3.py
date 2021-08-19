from collections import deque


def solve(st):
    s = deque(st)
    return any((s == deque(reversed(s)) for _ in range(len(st)) if not s.rotate(1)))
