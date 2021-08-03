from collections import defaultdict


def solve(arr):
    d = defaultdict(int)
    for x in arr:
        d[abs(x)] += x
    return next(k if k in arr else -k for k, v in d.items() if v != 0)
