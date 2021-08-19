from functools import reduce
from math import floor, sqrt


def f(n, l=3):
    if n < l:
        return
    for p in range(l, min(floor(sqrt(n)) + 1, 21)):
        if not n % p:
            for l in f(n // p, p):
                yield ([p] + l)
    if n <= 20:
        yield [n]


def eq_dice(l):
    return sum((1 for l in f(reduce(lambda p, n: p * n, l, 1)) if len(l) > 1)) - (len(l) > 1)
