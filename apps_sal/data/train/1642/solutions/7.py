import operator as op
from functools import reduce


def factors(n):
    div = 2
    d = dict()
    while n > (div - 1) ** 2:
        if n % div == 0:
            n = n // div
            if div in d:
                d[div] += 1
            else:
                d[div] = 1
        else:
            div += 1
    if n in d:
        d[n] += 1
    elif n > 1:
        d[n] = 1
    r = []
    for k in d.keys():
        r.append((k, d[k]))
    return r


def get_pascal(r):
    if r == 1:
        return [1]
    elif r == 2:
        return [1, 1]
    s = [1, 1]
    while len(s) < r:
        ns = [1]
        for i in range(len(s) - 1):
            ns.append(s[i] + s[i + 1])
        ns = ns + [1]
        s = ns
    return s


def ncr(n, r):
    if r > n:
        return 0
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom


def get_cases(r, k):
    p = get_pascal(r)
    sum_v = 0
    for (i, v) in enumerate(p):
        sum_v += v * ncr(k, i + 1)
    return sum_v


def multiply(n, k):
    if n == 1:
        return 1
    f = factors(n)
    s = 1
    for r in f:
        s *= get_cases(r[1], k)
    return s
