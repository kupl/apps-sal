from itertools import groupby


def sum_consecutives(xs):
    return [sum(g) for (_, g) in groupby(xs)]
