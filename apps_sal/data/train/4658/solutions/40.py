
from functools import reduce

def max_product(A, n):
    prod = lambda A : reduce(lambda a, b : a*b, A)
    return prod(sorted(A, reverse=True)[:n])
