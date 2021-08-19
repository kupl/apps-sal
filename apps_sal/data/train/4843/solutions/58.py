import itertools


def choose_best_sum(t, k, ls):
    li = []
    for x in itertools.combinations(ls, k):
        li.append(sum(x))
    m = -1
    for s in li:
        if s <= t and s > m:
            m = s
    return None if m == -1 else m
