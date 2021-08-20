from itertools import combinations
from functools import reduce


def choose_best_sum(t, k, ls):
    mx = -1
    res = []
    for c in combinations(ls, k):
        s = reduce(lambda x, y: x + y, c)
        if s >= mx and s <= t:
            res = [c, s]
            mx = s
    if res == []:
        return None
    else:
        return res[1]
