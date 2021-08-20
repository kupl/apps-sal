def starting_mark(height):
    gradient = (10.67 - 9.45) / (1.83 - 1.52)
    c = 10.67 - gradient * 1.83
    return round(gradient * height + c, 2)
