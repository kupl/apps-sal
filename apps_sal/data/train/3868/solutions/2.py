from itertools import combinations

def closest_sum(arr, target):
    return min(map(sum, combinations(arr, 3)), key=lambda s: abs(target-s))
