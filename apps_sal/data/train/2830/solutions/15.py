def db_sort(arr):
    a, b = filter(lambda x: isinstance(x, str), arr), filter(lambda x: isinstance(x, int), arr)
    return sorted(b) + sorted(a)
