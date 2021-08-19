def spot_diff(a, b):
    return [i for (i, j) in enumerate(zip(a, b)) if j[0] != j[1]]
