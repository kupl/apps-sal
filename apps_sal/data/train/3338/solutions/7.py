from itertools import groupby


def ones_counter(xs):
    return [sum(g) for (x, g) in groupby(xs) if x == 1]
