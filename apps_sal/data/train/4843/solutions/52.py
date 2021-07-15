def choose_best_sum(t, k, ls):
    from itertools import combinations
    combos = list(combinations(ls, k))

    qualify = [ x for x in combos if sum(x) <= t ]
    
    if not qualify:
        return None
    else:
        return(sum(max(qualify, key = sum)))
