def distribute(m, n):
    (q, r) = divmod(max(m, 0), max(n, 1))
    return [q + (i < r) for i in range(max(n, 0))]
