import itertools


def choose_best_sum(t, k, ls):
    return max([sum(row) for row in list(itertools.combinations(ls, k)) if sum(row) <= t], default=None)
