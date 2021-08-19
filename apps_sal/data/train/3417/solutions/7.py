from itertools import groupby
from functools import reduce


def cut_the_ropes(arr):
    return reduce(lambda a, g: a + [a[-1] - sum((1 for __ in g[1]))], groupby(sorted(arr)), [len(arr)])[:-1]
