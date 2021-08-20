def starting_mark(height):
    (x1, y1) = (1.52, 9.45)
    (x2, y2) = (1.83, 10.67)
    slope = (y2 - y1) / (x2 - x1)
    c = y2 - slope * x2
    return round(height * slope + c, 2)
