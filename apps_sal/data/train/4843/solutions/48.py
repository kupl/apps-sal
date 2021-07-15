import itertools

def choose_best_sum(t, k, ls):
    ansbos = None
    combos = list(itertools.combinations(ls, k))
    sumbos = sorted(list(map(sum, combos)))
    for c in sumbos:
        if c > t:
            return ansbos
        else:
            ansbos = c
    return ansbos
