from itertools import groupby
from operator import itemgetter

def solve(arr):
    s = sorted(((c, sorted(set(a))) for c, a in enumerate(arr)), key = itemgetter(1))
    return sorted(sum(map(itemgetter(0), a)) for a in (list(g) for _, g in groupby(s, itemgetter(1))) if len(a) > 1)
