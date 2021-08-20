def filter_homogenous(b):
    return [a for a in b if bool(a) and all([type(v1) == type(v2) for (v1, v2) in zip(a, a[1:])])]
