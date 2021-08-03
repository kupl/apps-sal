from itertools import combinations


def choose_best_sum(t, k, ls):
    result = sorted((sum(i) for i in combinations(ls, k) if sum(i) <= t))
    return result[-1] if result else None
