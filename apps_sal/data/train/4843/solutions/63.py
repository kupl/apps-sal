from itertools import combinations

def choose_best_sum(t, k, ls):
    variants=[x for x in combinations(ls,k) if sum(x)<=t]
    return max(sum(x) for x in variants) if variants!=[] else None
