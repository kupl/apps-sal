# return a sorted set with the difference
def diff(a, b):
    a = set(a)
    b = set(b)
    c = a.symmetric_difference(b)
    return sorted(list(c))
