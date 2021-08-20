def past(h, m, s):
    if not 0 <= h <= 23 or not 0 <= m <= 59 or (not 0 <= s <= 59):
        return 'Error'
    else:
        return h * 3600000 + m * 60000 + s * 1000
