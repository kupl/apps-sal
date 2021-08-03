from functools import lru_cache


@lru_cache(None)
def count_ways(n, k):
    return sum(count_ways(n - a, k) for a in range(1, min(n, k) + 1)) if n else 1
