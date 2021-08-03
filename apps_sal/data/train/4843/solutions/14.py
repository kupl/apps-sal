from itertools import combinations


def choose_best_sum(t, k, ls):
    sums = {sum(combination) for combination in combinations(ls, k) if sum(combination) <= t}
    return max(sums, default=None)
