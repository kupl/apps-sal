def lamps(a):
    n = sum(1 for i, x in enumerate(a) if x != i % 2)
    return min(n, len(a) - n)
