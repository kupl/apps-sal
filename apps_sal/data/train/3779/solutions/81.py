def past(h, m, s):
    x = 60 * 60 * 1000 * h + 60 * 1000 * m + 1000 * s
    if (0 <= h <= 23, 0 <= m <= 59, 0 <= s <= 59):
        return x
