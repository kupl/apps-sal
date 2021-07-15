def past(h, m, s):
    seconds = h * 3600 + m * 60 + s
    milliseconds = seconds * 1000
    return milliseconds
