def f(n, m):
    (q, r) = divmod(n, m)
    return q * m * (m - 1) // 2 + r * (r + 1) // 2
