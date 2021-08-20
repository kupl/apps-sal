from functools import lru_cache


@lru_cache(maxsize=None)
def count_ways(n, k):
    return n == 0 or sum((count_ways(n - x, k) for x in range(1, min(n, k) + 1)))
