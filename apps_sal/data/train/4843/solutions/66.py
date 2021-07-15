import itertools

def choose_best_sum(t, k, ls):
    arr = list(itertools.combinations(ls, k))
    new_arr = set([sum(item) for item in arr if sum(item) <= t])
    return max(new_arr) if len(new_arr) >= 1 else None
