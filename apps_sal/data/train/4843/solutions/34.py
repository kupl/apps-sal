import itertools


def choose_best_sum(t, k, ls):
    combinations = itertools.combinations(ls, k)
    a = list(combinations)
    b = [sum(c) for c in a]
    d = [i for i in b if i <= t]
    if not d:
        return (None)
    else:
        d_max = max(d)
        return(d_max)
