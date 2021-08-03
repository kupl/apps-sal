from collections import deque


def count_ways(n, k):
    s, d = 1, deque([0] * k)
    for i in range(n):
        d.append(s)
        s = 2 * s - d.popleft()
    return s - d.pop()
