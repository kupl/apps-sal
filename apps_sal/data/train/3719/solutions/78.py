def starting_mark(height):
    m = 1.22 / 0.31
    b = 10.67 - (1.83 * m)
    return float("{:.2f}".format(round(m * height + b, 2)))
