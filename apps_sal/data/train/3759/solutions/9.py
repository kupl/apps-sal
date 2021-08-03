import functools


def product_array(n):
    return [functools.reduce(lambda a, b: a * b, n) // x for x in n]
