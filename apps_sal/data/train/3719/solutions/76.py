def starting_mark(height):

    m = (10.67 - 9.45) / (1.83 - 1.52)
    c = 10.67 - m * 1.83

    return round(height * m + c, 2)
