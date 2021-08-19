def starting_mark(height):
    # y = ax + c
    a = (9.45 - 10.67) / (1.52 - 1.83)
    c = 9.45 - a * 1.52
    return round(a * height + c, 2)
