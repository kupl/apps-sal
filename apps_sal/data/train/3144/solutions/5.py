from itertools import groupby


def number_of_pairs(gloves):
    return sum([len(list(g)) // 2 for (k, g) in groupby(sorted(gloves))])
