from itertools import combinations


def choose_best_sum(t, k, ls):
    sums = list(map(sum, combinations(ls, k)))
    if t in sums:
        return t
    max_ = 0
    for i in sums:
        max_ = i if i < t and i > max_ else max_
    return None if max_ == 0 else max_
