def db_sort(arr):
    return sorted([x for x in arr if isinstance(x, int)]) + sorted([x for x in arr if isinstance(x, str)])
