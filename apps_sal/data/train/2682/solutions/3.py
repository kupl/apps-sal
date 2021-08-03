from math import factorial
from collections import Counter


def C(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)


def est_subsets(arr):
    s = set(arr)
    return sum(C(len(s), i) for i in range(1, len(s) + 1))
