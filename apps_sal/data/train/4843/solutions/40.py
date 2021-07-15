import itertools
def choose_best_sum(t, k, ls):
    ktowns = [sum(x) for x in list(itertools.combinations(ls,k)) if sum(x) <= t]
    return max(ktowns) if ktowns !=[] else None
