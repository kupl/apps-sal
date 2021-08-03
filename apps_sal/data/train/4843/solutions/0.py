import itertools


def choose_best_sum(t, k, ls):
    try:
        return max(sum(i) for i in itertools.combinations(ls, k) if sum(i) <= t)
    except:
        return None
