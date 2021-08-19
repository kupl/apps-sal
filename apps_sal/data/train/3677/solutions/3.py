def filter_homogenous(arrays):
    return [a for a in arrays if a and all((type(a[0]) == type(b) for b in a))]
