import math


def all_permuted(n):
    return n * all_permuted(n - 1) + (-1)**n if n > 2 else n - 1
