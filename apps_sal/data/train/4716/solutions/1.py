from collections import deque


def distribution_of(golds):
    g = deque(golds)
    s = [0, 0]
    t = 0
    while g:
        s[t] += (g.popleft, g.pop)[g[0] < g[-1]]()
        t ^= 1
    return list(s)
