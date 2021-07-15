def distribute(m, n):
    if n <= 0:
        return []
    if m < 0:
        m = 0
    q, r = divmod(m, n)
    return [q + 1] * r + [q] * (n - r)
