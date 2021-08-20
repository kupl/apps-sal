def f(n):
    if isinstance(n, int) and n >= 1:
        return n / 2 * (n + 1)
    else:
        return None
