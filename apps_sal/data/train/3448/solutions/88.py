def f(n):
    if isinstance(n, int) and n > 0:
        return (n * (2 + (n - 1))) / 2 if n > 0 else None
