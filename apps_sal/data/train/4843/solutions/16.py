from itertools import combinations

def choose_best_sum(t, k, ls):
    l= sorted([sum(x) for x in list(combinations(ls,k)) if sum(x) <=t])
    return l[-1] if l else None
