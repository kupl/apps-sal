from functools import reduce


def max_product(lst, n):
    return reduce(lambda a, b: a * b, sorted(lst)[-n:], 1)
