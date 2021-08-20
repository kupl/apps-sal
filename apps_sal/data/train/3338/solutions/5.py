from itertools import groupby


def ones_counter(lst):
    return [len(list(b)) for (a, b) in groupby(lst) if a]
