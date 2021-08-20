def past(h, m, s):
    a = 60
    b = 1000
    return h * a * a * b + m * a * b + s * b
