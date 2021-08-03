import itertools


def closest_sum(ints, num):
    res = ints[:3]
    comb = list(itertools.combinations(ints, 3))
    for i in comb:
        if abs(num - sum(i)) < abs(num - sum(res)):
            res = [_ for _ in i]
    return sum(res)
