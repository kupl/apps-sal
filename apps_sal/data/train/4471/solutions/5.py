def lamps(a):
    n = sum([1 for (x, y) in enumerate(a) if y == x % 2])
    return min(len(a) - n, n)
