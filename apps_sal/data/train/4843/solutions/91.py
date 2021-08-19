def choose_best_sum(t, k, ls):
    from itertools import combinations
    try:
        return max((s for s in map(sum, combinations(ls, k)) if s <= t))
    except ValueError:
        return None
