from math import gcd, sqrt
from functools import reduce


def scf(xs):
    try:
        d = reduce(gcd, xs)
    except TypeError:
        return 1
    else:
        return next((i for i in range(2, int(sqrt(d)) + 1) if d % i == 0), d)
