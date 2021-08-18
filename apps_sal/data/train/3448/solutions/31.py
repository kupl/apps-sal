def f(n):
    if isinstance(n, int) and n > 0:
        nn = [i for i in range(n + 1)]
        return sum(nn)
