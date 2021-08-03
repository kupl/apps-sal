import itertools


def choose_best_sum(t, k, ls):
    ls = [sum(seq) for seq in itertools.combinations(ls, k) if sum(seq) <= t]
    if ls:
        return max(ls)
    else:
        return None
    # your code
