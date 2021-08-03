from itertools import combinations


def choose_best_sum(n, k, ls):
    t = (sum(i) for i in combinations(ls, k))
    return max(filter(lambda x: x <= n, t), default=None)
