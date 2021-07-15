def choose_best_sum(t, k, ls):
    from itertools import combinations
    ls_ = [sum(x) for x in [*combinations(ls, k)] if sum(x) <= t]
    if len(ls_) == 0:
        return None
    else:
        return max(ls_)

