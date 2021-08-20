def squares(x, n):
    if n < 0:
        return []
    return [] if n == 0 else [x] + squares(x ** 2, n - 1)
