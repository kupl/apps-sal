from itertools import combinations


def choose_best_sum(t, k, ls):
    if k > len(ls):
        return None
    combos = list(combinations(ls, k))
    sums = [sum(x) for x in combos if sum(x) <= t]
    if sums:
        best = min(sums, key=lambda x: t - x)   # find smallest diff
        return best
    return None
