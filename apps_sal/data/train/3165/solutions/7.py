from math import log
from functools import lru_cache


@lru_cache(5000)
def toothpick(n):
    if n == 0:
        return 0
    else:
        k = int(log(n, 2))
        i = n - 2**k
        if i == 0:
            return (2**(2 * k + 1) + 1) / 3
        else:
            return toothpick(2**k) + 2 * toothpick(i) + toothpick(i + 1) - 1
