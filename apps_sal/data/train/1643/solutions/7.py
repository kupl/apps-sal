import functools
import sys


@functools.lru_cache(None)
def almost_everywhere_zero(n, k):
    n = str(n)
    if len(n) == 0 or k < 0:
        return k == 0
    d = int(n[0])
    return sum((almost_everywhere_zero(n[1:] if i == d else '9' * (len(n) - 1), k - 1 if i > 0 else k) for i in range(d + 1)))


sys.setrecursionlimit(100000)
