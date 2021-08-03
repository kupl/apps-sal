def db_sort(arr):
    return sorted(i for i in arr if isinstance(i, int)) + sorted(i for i in arr if isinstance(i, str))
