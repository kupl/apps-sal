def past(h, m, s):
    oclock1 = h * 3600000
    oclock2 = m * 60000
    oclock3 = s * 1000
    return oclock1 + oclock2 + oclock3
