def lamps(a):
    return min(sum((1 for (i, n) in enumerate(a) if n == i % 2)), sum((1 for (i, n) in enumerate(a) if n != i % 2)))
