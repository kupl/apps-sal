def two_highest(a):
    return [0, sorted(set(a))[:-3:-1]][type(a) == list]
