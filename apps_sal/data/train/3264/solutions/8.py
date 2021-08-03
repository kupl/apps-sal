from math import floor, log10


def count(n):
    n = n + 1
    return floor(sum(map(log10, range(2, n)))) + 1
