from collections import deque


def reorder(n, m):
    (a, b) = (deque(range(n // 2)), deque(range(n // 2, n)))
    a.rotate(m)
    b.rotate(m)
    return [list(a), list(b)]
