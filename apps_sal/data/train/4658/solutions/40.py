
from functools import reduce


def max_product(A, n):
    def prod(A): return reduce(lambda a, b: a * b, A)
    return prod(sorted(A, reverse=True)[:n])
