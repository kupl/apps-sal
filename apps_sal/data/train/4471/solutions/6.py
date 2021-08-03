def lamps(a):
    r = sum(x == c % 2 for c, x in enumerate(a))
    return min(r, len(a) - r)
