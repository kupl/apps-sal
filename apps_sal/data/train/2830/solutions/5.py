def db_sort(arr):
    return sorted((n for n in arr if type(n) is int)) + sorted((s for s in arr if type(s) is str))
