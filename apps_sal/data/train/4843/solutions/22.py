from itertools import combinations

def choose_best_sum(t, k, ls):
    return max((d for d in map(sum, combinations(ls, k)) if d <= t), default=None)
