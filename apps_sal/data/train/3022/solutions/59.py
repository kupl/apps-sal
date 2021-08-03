def two_highest(a):
    return a and sorted(set(a), reverse=True)[0:2]
