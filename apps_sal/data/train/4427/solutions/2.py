from itertools import groupby


def sum_groups(lst):
    l = -1
    while l != len(lst):
        l, lst = len(lst), [sum(g) for _, g in groupby(lst, key=lambda n: n % 2)]
    return l
