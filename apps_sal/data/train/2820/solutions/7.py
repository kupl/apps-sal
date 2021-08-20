def spot_diff(s1, s2):
    return [index for (index, (c1, c2)) in enumerate(zip(s1, s2)) if c1 != c2]
