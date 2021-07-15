from itertools import combinations
def choose_best_sum(t, k, ls):
    return max([sum(b) for b in combinations(ls, k) if sum(b) <= t], default=None)
