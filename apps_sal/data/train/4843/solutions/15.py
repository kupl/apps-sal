import itertools


def choose_best_sum(t, k, ls):
    if len(ls) < k:
        return
    a = list(itertools.combinations(ls, k))
    b = []
    c = []
    for i in a:
        b.append(sum(i))
    for i in b:
        if i <= t:
            d = t - i
            c.append(d)
    c.sort()
    if c == []:
        return
    else:
        return t - c[0]
        # your code
