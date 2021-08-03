from itertools import groupby


def sum_consecutives(s):
    return [sum(grp) for _, grp in groupby(s)]
