def int_diff(arr, n):
    return len([abs(x[0] - x[1]) for x in __import__('itertools').combinations(arr, 2) if abs(x[0] - x[1]) == n])
