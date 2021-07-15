from itertools import combinations

def choose_best_sum(t, k, ls):
    
    s = [sum(comb) for comb in combinations(ls, k) if sum(comb) <= t]
    
    return max(s) if len(s) > 0 else None

