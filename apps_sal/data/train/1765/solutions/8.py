from functools import lru_cache


def partitions(n):
    return sum(part(n, k) for k in range(1, n+1))


@lru_cache(maxsize=None)
def part(n, k):
    return 1 if k in {1, n} else sum(part(n-k, i) for i in range(1, min(n-k, k)+1))
