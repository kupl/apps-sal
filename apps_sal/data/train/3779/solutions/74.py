def past(h, m, s):
    while 0 <= h <= 23 and 0 <= m <= 59 and (0 <= s <= 59):
        h *= 3600000
        m *= 60000
        s *= 1000
        return h + m + s
