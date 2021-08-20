import math
from itertools import combinations


def choose_best_sum(t, k, ls):
    comb = combinations(ls, k)
    max = None
    for l in comb:
        s = sum(l)
        if s > t:
            continue
        if max == None:
            max = s
            continue
        if max < s:
            max = s
    return max


def choose_best_sumx(t, k, ls):
    result = choose_best_sum_recursion(t, k, ls)
    if result == -math.inf:
        return None
    return result


def choose_best_sum_recursion(t, k, ls):
    if t < 0:
        return -math.inf
    if k == 0 and t >= 0:
        return 0
    max = -math.inf
    for (idx, item) in enumerate(ls):
        l = [x for (i, x) in enumerate(ls) if i != idx]
        result = item + choose_best_sum_recursion(t - item, k - 1, l)
        if result > max:
            max = result
    return max
