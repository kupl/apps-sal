from itertools import count
from functools import lru_cache

L = list(range(11))
S = set(L)

@lru_cache(maxsize=None)
def to_set(x): return set(str(x))

def find_num(n):
    while n >= len(L):
        x = next(filter(lambda i: not (i in S or to_set(L[-1]) & to_set(i)), count()))
        L.append(x)
        S.add(x)
    return L[n]
