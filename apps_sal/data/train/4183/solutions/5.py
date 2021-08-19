def greatest_distance(a):
    return max((i - a.index(e) for (i, e) in enumerate(a)))
