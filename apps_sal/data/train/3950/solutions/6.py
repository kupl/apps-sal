from itertools import combinations
from functools import lru_cache


@lru_cache(maxsize=None)
def factors(x):
    return {v for i in range(2, int(x**0.5) + 1) if not x % i for v in (i, x // i)}


@lru_cache(maxsize=None)
def nb_common_div(s):
    l = len(s)
    s1 = sum(int(''.join(v)) for i in range(l) for v in combinations(s, i + 1))
    s2 = sum(int(''.join(s[i:j + 1])) for i in range(l) for j in range(i, l))
    f1, f2 = factors(s1), factors(s2)
    return len(f1 & f2)


def find_int_inrange(a, b):
    best, res = -1, []
    for x in range(a, b + 1):
        nb = nb_common_div(str(x))
        if nb > best:
            best, res = nb, [nb, x]
        elif nb == best:
            res.append(x)
    return res
