from itertools import groupby


def find_needed_guards(k):
    return sum(len(list(g)) // 2 for v, g in groupby(k) if v == 0)
