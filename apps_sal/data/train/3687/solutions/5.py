import functools


def gcd_rec(a, b):
    if b:
        return gcd_rec(b, a % b)
    else:
        return a


def mn_lcm(m, n):
    lst = list(range(min(n, m), max(n, m) + 1))
    return functools.reduce(lambda a, b: a * b / gcd_rec(a, b), lst)
