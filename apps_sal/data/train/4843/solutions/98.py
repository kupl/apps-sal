import itertools


def choose_best_sum(t, k, ls):
    result = [sum(seq) for seq in itertools.combinations(ls, k) if sum(seq) <= t]
    if len(result) == 0:
        return None
    else:
        return max(result)
