from functools import lru_cache


@lru_cache(maxsize=None)
def count_ways(n, k):
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    return sum((count_ways(n - i, k) for i in range(1, k + 1)))
