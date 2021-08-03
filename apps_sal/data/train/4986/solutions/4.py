def f(n, m):
    x, y = divmod(n, m)
    return x * m * (m - 1) / 2 + y * (y + 1) / 2
