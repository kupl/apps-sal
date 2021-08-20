def twos_difference(a):
    s = set(a)
    return sorted(((x, x + 2) for x in a if x + 2 in s))
