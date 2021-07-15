import sys
import functools
sys.setrecursionlimit(1_000_000)

# lru_cache is a python shortcut for memoization
# memoization is a technique to avoid repeatedly calculating
# something that has already been calculated

@functools.lru_cache(maxsize=1_000_000)
def choose(n,k):
    # pascals triangle uses only addition
    # so no rounding
    #               1
    #              1 1
    #             1 2 1
    #            1 3 3 1
    #           1 4 6 4 1
    # with exception of edge cases
    # this has recursive formula
    # choose(n, k) = choose(n-1, k-1) + choose(n-1, k)
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return choose(n-1, k-1) + choose(n-1, k)
