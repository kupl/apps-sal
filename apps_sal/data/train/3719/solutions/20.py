def starting_mark(height):
    x = 1.22 / .31
    f = 9.45 - 1.52 * x
    return round(height * x + f, 2)
