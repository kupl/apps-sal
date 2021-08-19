def greatest_distance(a):
    return max((len(a) - a[::-1].index(e) - a.index(e) - 1 for e in a))
