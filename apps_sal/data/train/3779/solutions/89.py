def past(h, m, s):
    totalseconds = s + h * 3600 + m * 60
    milliseconds = totalseconds * 1000
    return milliseconds
