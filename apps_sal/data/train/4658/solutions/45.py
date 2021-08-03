from functools import reduce


def max_product(L, k):
    return reduce(lambda a, b: a * b, sorted(L, reverse=True)[:k])
