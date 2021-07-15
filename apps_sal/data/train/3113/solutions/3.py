def distribute(m, n):
    if n <= 0:
        return []
    d, r = divmod(max(m, 0), n)
    return r * [d + 1] + (n - r) * [d]
