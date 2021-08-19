def spot_diff(s1, s2):
    return [i for (i, (x, y)) in enumerate(zip(s1, s2)) if x != y]
