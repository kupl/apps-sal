import operator
import functools


def parameter(n):
    ls = [int(i) for i in str(n)]
    m = functools.reduce(operator.mul, ls)
    s = sum(ls)
    return m * s / gcd(m, s)


def gcd(a, b):
    if not b:
        return a
    else:
        return gcd(b, a % b)
