from itertools import groupby


def group_ints(lst, key=0):
    return [list(grp) for k, grp in groupby(lst, key=lambda x: x < key)]
