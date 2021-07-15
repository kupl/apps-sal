import itertools

def choose_best_sum(t, k, ls):
    return max([None] + filter(lambda x: x <= t, map(sum, itertools.combinations(ls, k))))
