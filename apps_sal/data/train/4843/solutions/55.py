import itertools


def choose_best_sum(t, k, ls):
    largest = 0
    for comb in itertools.combinations(ls, k):
        if sum(comb) > largest and sum(comb) <= t:
            largest = sum(comb)
    return largest if largest > 0 else None
