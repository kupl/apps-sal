from math import gcd


def lcm(x, y):
    return x * y // gcd(x, y)


def DPC_sequence(s):
    res = 1
    for (i, x) in enumerate(s):
        if x == 'D':
            res = lcm(res, i + 1)
    for (i, x) in enumerate(s):
        if x == 'C' and (not res % (i + 1) or gcd(res, i + 1) == 1) or (x == 'P' and gcd(res, i + 1) > 1):
            return -1
    return res
