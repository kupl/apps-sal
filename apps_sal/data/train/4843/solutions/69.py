import itertools


def choose_best_sum(t, k, ls):
    filtered = list([x for x in ls if x <= t])
    mutations = list(itertools.combinations(filtered, k))
    if not mutations:
        return None
    sums = list([x for x in [sum(m) for m in mutations] if x <= t])
    if not sums:
        return None
    return max(sums)
