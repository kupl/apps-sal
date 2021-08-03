import math


def getDivisors(n):
    divisors = set()
    e = 1
    while e <= math.sqrt(n):
        if n % e == 0:
            divisors.update([e, n / e])
        e += 1
    return divisors


def buildDict(n_max):
    res = {}
    for i in range(1, n_max):
        res[i] = len(getDivisors(i))
    return res


def count_pairs_int(diff, n_max):
    d = buildDict(n_max)
    x = 0
    for n in range(n_max):
        if d.get(n, 0) == d.get(n + diff, 0):
            x += 1
    return x
