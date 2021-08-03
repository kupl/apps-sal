import itertools as it


def choose_best_sum(t, k, ls):
    if len(ls) > 0:
        combs = [sum(i) for i in list(it.combinations(ls, k)) if sum(i) <= t]
    try:
        return(max(combs))
    except:
        return(None)
