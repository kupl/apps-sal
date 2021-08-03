def starting_mark(height):
    slope = 1.22 / 0.31
    offset = 9.45 - slope * 1.52
    result = round(slope * height + offset, 2)
    return result
