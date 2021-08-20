import sys
import functools
sys.setrecursionlimit(1000000)


@functools.lru_cache(maxsize=1000000)
def choose(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return choose(n - 1, k - 1) + choose(n - 1, k)
