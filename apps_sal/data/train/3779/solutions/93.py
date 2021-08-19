def past(h, m, s):
    if 0 <= h <= 23 and 0 <= m <= 59 and (0 <= s <= 59):
        h = h * 60 * 60 * 1000
        m = m * 60 * 1000
        s = s * 1000
        return h + m + s
