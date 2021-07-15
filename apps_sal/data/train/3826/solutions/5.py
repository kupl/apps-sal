def cycle(n):
    if not (n%2 and n%5): return -1
    return next(filter(lambda x: pow(10, x, n) == 1, range(1, n)))
