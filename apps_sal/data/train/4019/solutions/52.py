def max_multiple(d, b):
    return next(n for n in range(b, 0, -1) if n % d == 0)
