from itertools import combinations


def choose_best_sum(t, k, ls):
    return max((s for s in map(sum, combinations(ls, k)) if s <= t), default=None)
