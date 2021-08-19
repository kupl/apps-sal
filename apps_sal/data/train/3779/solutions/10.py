def past(h, m, s):
    if 0 <= h <= 23 and 0 <= m <= 59 and (0 <= s <= 59):
        L = []
        L.append(h * 3600000)
        L.append(m * 60000)
        L.append(s * 1000)
        return sum(L)
