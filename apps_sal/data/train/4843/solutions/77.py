def choose_best_sum(t, k, ls):
    import itertools
    combinations = [sum(i) for i in itertools.combinations(ls,k) if sum(i) <= t]
    if len(combinations) == 0:
        return None
    return max(combinations)
