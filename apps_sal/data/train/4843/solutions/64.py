import itertools


def choose_best_sum(t, k, ls):
    d = itertools.combinations(ls, k)
    d = [list(x) for x in d]
    d = list(k for k, _ in itertools.groupby(d))
    d.sort(key=lambda x: sum(x))

    res = sum(d[0]) if len(d) > 0 and sum(d[0]) <= t else None

    for i in range(1, len(d)):
        if sum(d[i]) > t:
            break
        else:
            res = sum(d[i])

    return res
