def past(h, m, s):
    if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
        return (s + 60 * (60 * h + m)) * 1000
