def past(h, m, s):
    ms = s * 1000
    mm = m * 60000
    mh = h * 3600000
    return ms + mm + mh
