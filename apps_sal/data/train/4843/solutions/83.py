from itertools import combinations

def choose_best_sum(t, k, ls):
    if len(ls)<k:
        return None
    best_sum = max([sum(c) if sum(c)<=t else 0 for c in combinations(ls, k)])
    return best_sum if best_sum else None

