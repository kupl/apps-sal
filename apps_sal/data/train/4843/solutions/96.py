from itertools import combinations


def choose_best_sum(t, k, ls):
    a = sorted([sum(i) for i in combinations(ls, k)])
    for i in a[::-1]:
        if i <= t:
            return i
    return None
