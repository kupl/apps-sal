import itertools


def sum_consecutives(s):
    return [sum(num) for (g, num) in itertools.groupby(s)]
