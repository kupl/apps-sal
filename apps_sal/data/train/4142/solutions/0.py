from collections import defaultdict


def solve(arr):
    dct = defaultdict(list)
    for i, fs in enumerate(map(frozenset, arr)):
        dct[fs].append(i)
    return sorted(sum(lst) for lst in dct.values() if len(lst) > 1)
