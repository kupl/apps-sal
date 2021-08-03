# return a sorted set with the difference
def diff(a, b):
    return sorted(set(a).symmetric_difference(set(b)))
