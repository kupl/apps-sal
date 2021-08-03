from math import floor, sqrt
from numpy import prod


def f(n, l=3):
    if n < l:
        return
    for p in range(l, min(floor(sqrt(n)) + 1, 21)):
        if not n % p:
            for l in f(n // p, p):
                yield [p] + l
    if n <= 20:
        yield [n]


def eq_dice(l):
    return sum(1 for l in f(prod(l)) if len(l) > 1) - (len(l) > 1)
