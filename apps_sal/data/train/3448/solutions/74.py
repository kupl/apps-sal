def f(n):
    if isinstance(n, int) and n > 0:
        return sum(x for x in range(1, n + 1))
