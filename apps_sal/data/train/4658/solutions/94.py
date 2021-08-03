from functools import reduce


def max_product(lst, nl):
    return reduce(lambda x, y: x * y, sorted(lst, reverse=True)[:nl])
