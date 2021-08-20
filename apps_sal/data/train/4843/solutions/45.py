import itertools


def choose_best_sum(t, k, ls):
    if len(ls) < k:
        return None
    towns = [x for x in ls if x <= t]
    comb = itertools.combinations(towns, k)
    prev_best = 0
    for s in comb:
        sum_cand = sum(s)
        if sum_cand == t:
            return sum_cand
        elif prev_best < sum_cand and sum_cand < t:
            prev_best = sum_cand
    if prev_best > t or prev_best == 0:
        return None
    else:
        return prev_best
