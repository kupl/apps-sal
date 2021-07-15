def starting_mark(height):
    slope = (9.45 - 10.67) / (1.52 - 1.83)
    intercept = 9.45 - (1.52 * slope)
    return round(slope * height + intercept, 2)
