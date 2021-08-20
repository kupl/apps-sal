import itertools


def choose_best_sum(t, k, ls):
    p = list(ls)
    a = itertools.combinations(p, k)
    x = 0
    c = 0
    p.sort()
    if k > len(ls):
        return None
    for i in range(k):
        c = c + p[i]
        if i + 1 == len(ls):
            break
    if c > t:
        return None
    for i in a:
        if sum(i) <= t and t - sum(i) < t - x:
            x = sum(i)
    return x
