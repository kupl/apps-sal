def db_sort(xs):
    return sorted(xs, key=lambda x: (isinstance(x, str), x))
