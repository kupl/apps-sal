import itertools

def choose_best_sum(t, k, ls):
    sums = filter(lambda x: x <= t, map(sum, itertools.combinations(ls, k)))
    if sums:
        return max(sums)
    return None
