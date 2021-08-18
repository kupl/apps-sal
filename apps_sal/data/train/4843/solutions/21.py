def choose_best_sum(t, k, ls):
    from itertools import combinations
    comb = list(combinations(ls, k))
    sums = [sum(i) for i in comb]
    try:
        return max([i for i in sums if i <= t])
    except:
        return None
