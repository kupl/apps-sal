from itertools import combinations as comb
from functools import reduce

def choose_best_sum(t, k, ls):
    return reduce(lambda s, e: max(sum(e), s) if sum(e) <= t else s, comb(ls, k), None)

