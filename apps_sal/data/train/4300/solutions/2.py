from functools import lru_cache


def solve(a, b):
    l_a, l_b, rec = len(a), len(b), lru_cache(maxsize=None)(lambda x, y: (x == l_a) or sum(rec(x + 1, i + 1) for i in range(y, l_b) if b[i] == a[x]))
    return rec(0, 0)
