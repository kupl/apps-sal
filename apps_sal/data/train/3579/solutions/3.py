from functools import reduce
from math import factorial


def choose(n, k):
    return reduce(int.__mul__, range(n - k + 1, n + 1), 1) // factorial(k)
