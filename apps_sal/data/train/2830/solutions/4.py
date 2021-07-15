def db_sort(xs): 
    return sorted(xs, key=lambda x: (type(x) is str, x))
