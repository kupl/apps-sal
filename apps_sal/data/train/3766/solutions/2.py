from collections import defaultdict
from functools import lru_cache
from itertools import chain

@lru_cache(maxsize=None)
def factors(n):
    if n == 1: return [(1, 1)]
    res, wheel = defaultdict(int), [1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6]
    x, y = 2, 0
    while x*x <= n:
        if not n%x:
            res[x] += 1
            n //= x
        else:
            x += wheel[y]
            y = 3 if y == 10 else y+1
    res[n] += 1
    return res.items()

def getAllPrimeFactors(n):
    return list(chain.from_iterable([k]*v for k,v in factors(n))) if isinstance(n, int) and n > 0 else []

def getUniquePrimeFactorsWithCount(n):
    return list(map(list, zip(*factors(n)))) if isinstance(n, int) and n > 0 else [[], []]

def getUniquePrimeFactorsWithProducts(n):
    return [k**v for k,v in factors(n)] if isinstance(n, int) and n > 0 else []
