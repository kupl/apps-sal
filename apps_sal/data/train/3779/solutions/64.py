def past(h, m, s):
    output = 0
    time = 0

    time = ((h * 60) * 60 + (m * 60) + s)

    return time * 1000
