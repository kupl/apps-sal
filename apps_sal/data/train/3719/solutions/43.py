def starting_mark(height):
    slope = (10.67 - 9.45) / (1.83 - 1.52)
    c = 10.67 - slope * 1.83
    return round(slope * height + c, 2)
