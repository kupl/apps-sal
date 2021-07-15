from itertools import groupby


def sum_consecutives(lst):
    return [sum(g) for _, g in groupby(lst)]
