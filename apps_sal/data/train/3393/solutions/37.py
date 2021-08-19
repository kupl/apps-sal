from math import sqrt, pow
from functools import reduce


def list_squared(m, n):

    def sqr_sum(i):
        return sum(set(reduce(list.__add__, ([pow(j, 2), pow(i // j, 2)] for j in range(1, int(sqrt(i)) + 1) if i % j == 0))))
    return [[i, j] for (i, j) in zip(range(m, n + 1), map(sqr_sum, range(m, n + 1))) if sqrt(j) == int(sqrt(j))]
