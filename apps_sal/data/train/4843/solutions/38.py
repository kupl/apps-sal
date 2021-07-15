from itertools import combinations
def choose_best_sum(t, k, ls): 
    combs = [sum(n) for n in combinations(ls, k) if sum(n)<=t]
    if len(combs) == 0:
        return None
    else:
        return max(combs)

