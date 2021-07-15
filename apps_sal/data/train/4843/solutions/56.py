import itertools

def choose_best_sum(t, k, ls):
    distances_sums = [sum(distances) for distances in set(itertools.combinations(ls, k)) if sum(distances) <= t] 
    return None if not distances_sums else max(distances_sums) 

