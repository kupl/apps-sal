def array_diff(a, b):
    set_b = set(b)
    return [i for i in a if i not in set_b]
