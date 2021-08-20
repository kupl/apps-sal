from collections import Counter
from itertools import groupby


def unpack_fun(l):
    return sorted([k for (k, v) in l for i in range(v)])


def solve(arr):
    out_lst = []
    l = [list(v) for (k, v) in groupby(Counter(arr).most_common(), key=lambda x: x[1])]
    for v in l:
        out_lst.extend(unpack_fun(v))
    return out_lst
