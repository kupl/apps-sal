def db_sort(arr):
    return sorted([v for v in arr if type(v) is int]) + sorted([v for v in arr if type(v) is str])
