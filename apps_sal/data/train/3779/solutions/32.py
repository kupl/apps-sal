def past(h, m, s):
    seconds = s + m * 60 + h * 3600
    return seconds / 0.001
