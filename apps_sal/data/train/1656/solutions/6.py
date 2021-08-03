from functools import lru_cache


def count_subsequences(a, b):
    n, m = len(a), len(b)

    @lru_cache(maxsize=None)
    def f(i, j):
        if j < i:
            return 0
        if i == 0:
            return 1
        return f(i, j - 1) + (f(i - 1, j - 1) if a[i - 1] == b[j - 1] else 0)

    return f(n, m) % 100_000_000
