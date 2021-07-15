from itertools import combinations

def choose_best_sum(t, k, ls):
    return max((n for n in (sum(v) for v in list(combinations(ls, k))) if n <=t), default=None)
