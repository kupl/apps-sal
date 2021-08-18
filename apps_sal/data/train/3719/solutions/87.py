def starting_mark(height):
    a = 1.22 / 0.31
    b = 9.45 - 1.52 * a
    return round(a * height + b, 2)
