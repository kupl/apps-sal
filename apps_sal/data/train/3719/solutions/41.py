def starting_mark(height):
    m = (10.67 - 9.45) / (1.83 - 1.52)
    return round((m * height + 10.67 - m * 1.83) * 100 / 100, 2)
