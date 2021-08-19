def rounding(n, m):
    (q, r) = divmod(n, m)
    return q * m if 2 * r < m else (q + 1) * m if 2 * r > m else n
