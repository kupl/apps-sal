from itertools import combinations


def choose_best_sum(t, k, ls):
    max = 0
    for subset in combinations(ls, k):
        s = sum(subset)
        if s > max and s <= t:
            max = s
    if max > 0:
        return max
    else:
        return None
