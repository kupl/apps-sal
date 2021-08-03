from itertools import groupby


def unique_in_order(iterable):
    return [x for (x, _) in groupby(iterable)]
