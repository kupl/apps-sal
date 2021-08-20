from functools import reduce


def min_value(d):
    return reduce(lambda a, b: a * 10 + b, sorted(set(d)))
