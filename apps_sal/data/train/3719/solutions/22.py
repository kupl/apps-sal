def starting_mark(height):
    a = (10.67 - 9.45) / (1.83 - 1.52)
    b = 10.67 - 1.22 / 0.31 * 1.83
    return round(height * a + b, 2)
