from collections import deque


def josephus(items, k):
    q = deque(items)
    return [[q.rotate(1 - k), q.popleft()][1] for _ in items]
