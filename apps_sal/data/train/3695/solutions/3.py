from itertools import groupby


def repeat_adjacent(string):
    return sum((1 for (k, g) in groupby((min(2, len(list(grp))) for (_, grp) in groupby(string))) if k == 2 and len(list(g)) > 1))
