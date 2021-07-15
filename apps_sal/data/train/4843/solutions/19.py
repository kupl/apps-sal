from itertools import combinations

def choose_best_sum(max_distance, k, distances):
    return max([sum(comb)
                for comb in combinations(distances, k)
                if sum(comb) <= max_distance], default=None)
