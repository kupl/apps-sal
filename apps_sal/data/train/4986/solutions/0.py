def f(n, m):
    re, c = divmod(n, m)
    return m * (m - 1) / 2 * re + (c + 1) * c / 2
