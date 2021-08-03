import operator as op
from functools import reduce


def Combi(n, k):
    if k > n:
        return 0
    k1, k2 = sorted((k, n - k))
    num = reduce(op.mul, range(n, k2, -1), 1)
    d = reduce(op.mul, range(1, k1 + 1), 1)
    return num // d


def bouncy_count(n):
    if n <= 2:
        return 0
    return 10**n - (Combi(n + 10, 10) + Combi(n + 9, 9) - 2 - 10 * n + 1)
