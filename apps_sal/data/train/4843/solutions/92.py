from itertools import combinations

def choose_best_sum(t, k, ls):
    routes = combinations(ls, k)
    sums = sorted([x for x in list(map(sum, routes)) if x <= t])
    if sums: return sums[-1]
    

