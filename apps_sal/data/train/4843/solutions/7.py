from itertools import combinations

def choose_best_sum(max_distance, k, distances):
    best = 0
    for combination in combinations(distances, k):
        distance = sum(combination)
        if distance == max_distance:
            return distance
        if distance < max_distance:
            best = max(best, distance)
    return best if best > 0 else None
