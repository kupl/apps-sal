def past(h, m, s):
    (0 <= h <= 23, 0 <= m <= 59, 0 <= s <= 59)
    m = int(m + h * 60)
    return int(s + m * 60) * 1000
