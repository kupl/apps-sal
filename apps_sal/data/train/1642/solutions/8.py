
from collections import Counter
from functools import lru_cache, reduce
from itertools import combinations
from operator import mul
from math import factorial


def multiply(n, k):
    if k < 2:
        return k
    if k == 2:
        return len(factors(n))
    tups = get_factor_tuples(n, k)
    tups = {tuple((1,) * (k - len(x)) + x) for x in tups}
    f = factorial(k)
    return sum(f // reduce(mul, [factorial(v) for v in list(Counter(p).values()) if v > 1] + [1]) for p in tups)


def get_factor_tuples(n, k):
    pair = {(n,)}
    for kp in range(1, k):
        k_tup = set(x for x in pair if len(x) == kp)
        for grp in k_tup:
            for i, e in enumerate(grp):
                g = grp[:i] + grp[i + 1:]
                if e not in primefactors(n):
                    for a in factors(e):
                        if 1 < a < e:
                            b = e // a
                            pair.add(tuple(sorted((a, b) + g)))
    return pair


@lru_cache(maxsize=None)
def primefactors(n):
    i, f = 3, []
    while n & 1 == 0:
        f.append(2)
        n = n >> 1
    while i * i <= n:
        if n % i:
            i += 2
        else:
            f.append(i)
            n //= i
    if n > 1:
        f.append(n)
    return f


@lru_cache(maxsize=None)
def factors(n):
    pf = primefactors(n)
    return {1, n} | {reduce(mul, x) for z in range(1, len(pf)) for x in combinations(pf, z)}
