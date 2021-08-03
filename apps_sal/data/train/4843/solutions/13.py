import itertools


def choose_best_sum(t, k, ls):
    list = []
    for c in itertools.combinations(ls, k):
        if sum(c) <= t:
            list.append(sum(c))
    return sorted(list)[-1] if len(list) >= 1 else None
