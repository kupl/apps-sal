from math import sqrt
from functools import reduce


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def list_squared(m, n):
    l = []
    for i in range(m, n):
        s = sum([x**2 for x in factors(i)])
        if sqrt(s) == int(sqrt(s)):
            l.append([i, s])
    return l
