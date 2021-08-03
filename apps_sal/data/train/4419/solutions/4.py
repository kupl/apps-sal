from itertools import product


def reg_sum_hits(n, s):
    d = {}
    for i in product(*[list(range(1, s + 1))] * n):
        r = sum(i)
        d[r] = d.get(r, 0) + 1
    return list(map(list, d.items()))
