from itertools import combinations


def choose_best_sum(t, k, ls):
    return max((sum(v) for v in combinations(ls, k) if sum(v) <= t), default=None)
