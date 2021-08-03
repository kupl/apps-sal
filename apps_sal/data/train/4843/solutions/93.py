from itertools import combinations


def choose_best_sum(t, k, ls):
    try:
        return min((abs(sum(x) - t), sum(x)) for x in combinations(ls, k) if sum(x) - t <= 0)[1]
    except ValueError:
        return None
