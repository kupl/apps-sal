from itertools import groupby


def group_ints(lst, key=0):
    return [list(g) for _, g in groupby(lst, key.__gt__)]
