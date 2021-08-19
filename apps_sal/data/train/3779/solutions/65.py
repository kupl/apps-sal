def past(h, m, s):
    assert 0 <= h <= 23 and 0 <= m <= 59 and (0 <= s <= 59)
    return h * 3600000 + m * 60000 + s * 1000
