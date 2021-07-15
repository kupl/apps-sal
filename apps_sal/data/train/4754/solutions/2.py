def group_ints(lst, key=0):
    from itertools import groupby
    return [list(group) for _, group in groupby(lst, lambda v: v >= key)]

