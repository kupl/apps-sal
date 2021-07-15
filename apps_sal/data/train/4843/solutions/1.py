from itertools import combinations

def choose_best_sum(t, k, ls):
    return max((s for s in (sum(dists) for dists in combinations(ls, k)) if s <= t), default=None)
