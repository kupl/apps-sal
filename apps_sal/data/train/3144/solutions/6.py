from itertools import groupby


def number_of_pairs(gloves):
    return sum((len(list(gp)) // 2 for (_, gp) in groupby(sorted(gloves))))
