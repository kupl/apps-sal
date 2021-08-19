from itertools import accumulate, chain, groupby


def cut_the_ropes(arr):
    return list(accumulate(chain((len(arr),), groupby(sorted(arr))), lambda a, b: a - sum((1 for __ in b[1]))))[:-1]
