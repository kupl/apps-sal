from functools import reduce


def max_product(lst, n):
    res = sorted(lst)[-n:]
    return reduce(lambda x, y: x * y, res)
