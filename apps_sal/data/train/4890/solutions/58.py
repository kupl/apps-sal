from numpy import prod


def find_difference(a, b):
    v1 = prod(a)
    v2 = prod(b)
    return abs(v1 - v2)
