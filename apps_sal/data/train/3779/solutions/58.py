def past(h, m, s):
    result = h * 3600 + m * 60 + s
    millisec = result * 1000
    return millisec
