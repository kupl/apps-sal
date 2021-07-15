def mystery_range(s,n):
    t = len(s) - 180
    m = n - 90
    x, xr = divmod(3 * m - t, 2)
    y, yr = divmod(t - m, 2)
    if (0 <= m <= t <= 3 * m and xr == 0 and yr == 0):
        return [10 - x, 99 + y]

    q, r = divmod(len(s), n)
    if (r != 0):
        return [10 ** q - n + r, 10 ** q - 1 + r]

    seq = [int(s[i * q : (i + 1) * q]) for i in range(0, n)]
    return [min(seq), max(seq)]
