A = (10.67 - 9.45) / (1.83 - 1.52)
B = 9.45 - A * 1.52


def starting_mark(height):
    return round(A * height + B, 2)
