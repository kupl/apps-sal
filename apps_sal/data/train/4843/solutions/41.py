import itertools


def choose_best_sum(t, k, ls):
    combos = set(list(itertools.combinations(ls, k)))
    sums = []
    for combo in combos:
        if sum(combo) <= t:
            sums.append(sum(combo))
    if sums:
        return max(sums)
