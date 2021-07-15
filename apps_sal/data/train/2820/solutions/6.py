def spot_diff(s1, s2):
    return [i for i, a in enumerate(zip(s1, s2)) if a[0] != a[1]]
