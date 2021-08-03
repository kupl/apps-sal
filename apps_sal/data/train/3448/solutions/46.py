def f(n):
    return sum(i for i in range(int(n) + 1)) if isinstance(n, int) and n > 0 else None
