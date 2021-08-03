def f(n):
    return int((((n**2) - 1) + (1 + n)) / 2) if isinstance(n, int) and n > 0 else None
