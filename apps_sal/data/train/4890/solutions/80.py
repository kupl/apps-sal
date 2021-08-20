from functools import reduce


def vol(l):
    return reduce(lambda x, y: x * y, l)


def find_difference(a, b):
    return abs(vol(b) - vol(a))
