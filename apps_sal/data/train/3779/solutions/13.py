def past(h, m, s):
    h = h * 3600
    m = m * 60
    s = s * 1
    milisec = h + m + s
    mil = str(milisec)
    mili = mil.ljust(3 + len(mil), '0')
    return int(mili)
