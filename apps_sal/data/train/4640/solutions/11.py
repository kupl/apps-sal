from itertools import combinations

def int_diff(arr, n):
    return sum(1 for a, b  in combinations(arr, 2) if abs(a - b) == n)
