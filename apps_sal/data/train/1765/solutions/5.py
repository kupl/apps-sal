from functools import lru_cache


@lru_cache(maxsize=None)
def partitions(n, start=1):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    return sum(partitions(n - i, i) for i in range(start, n + 1))
