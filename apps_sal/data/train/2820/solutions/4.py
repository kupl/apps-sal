def spot_diff(s1, s2):
    return [i for (i, (a, b)) in enumerate(zip(s1, s2)) if a != b]
