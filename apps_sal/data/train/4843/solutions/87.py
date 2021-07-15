def choose_best_sum(t, k, ls):
    from itertools import combinations

    i = [sum(a) for a in list(combinations(ls,k))]
    i.sort()
    result = None
    for a in i:
        if a <= t:
            result = a
    return(result)
