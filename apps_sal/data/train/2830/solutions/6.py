def db_sort(a):
    return sorted(a, key=lambda x: (type(x) is str, x))
