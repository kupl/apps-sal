def db_sort(arr):
    return sorted([x for x in arr if not isinstance(x, str)]) + sorted([x for x in arr if isinstance(x, str)])
