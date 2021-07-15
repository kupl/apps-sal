def starting_mark(height):
    slope = (10.67 - 9.45) / (1.83 - 1.52)
    intercept = 9.45 - 1.52 * slope
    return round(slope * height + intercept, 2)
