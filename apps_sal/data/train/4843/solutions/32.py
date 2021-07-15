from itertools import combinations

def choose_best_sum(t, k, ls):
    # your code
    s = [sum(i) for i in list(combinations(ls, k)) if sum(i) <= t]
    return max(s) if s != [] else None
