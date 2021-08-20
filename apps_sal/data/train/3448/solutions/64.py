def f(n):
    if isinstance(n, int) and n > 0:
        return int(n / 2 * (1 + n))
