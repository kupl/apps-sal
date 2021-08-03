from functools import reduce


def product_array(l):
    return [reduce(lambda p, n: p * n, l, 1) / n for n in l]
