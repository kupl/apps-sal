from itertools import combinations


def choose_best_sum(t, k, ls):
    a = list((i for i in combinations(ls, k) if sum(i) <= t))
    a.sort(key=lambda x: sum(x))
    if a:
        return sum(a[-1])
