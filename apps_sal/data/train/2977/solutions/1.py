import operator as op
from functools import reduce


def memoize(func):
    cache = {}

    def newfunc(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return newfunc


@memoize
def factors_of(n):
    result = []
    i = 2
    while i <= n:
        if n % i == 0:
            multiplicity = 0
            while n % i == 0:
                n = n / i
                multiplicity += 1
            result.append((i, multiplicity))
        i += 1
    return result


def filter_func(n):
    factors = factors_of(n)
    pfs = sum((p * i for (p, i) in factors))
    ds = reduce(op.mul, ((p ** (i + 1) - 1) / (p - 1) for (p, i) in factors))
    return ds % pfs == 0


def ds_multof_pfs(nMin, nMax):
    return list(filter(filter_func, range(nMin, nMax + 1)))[:]
