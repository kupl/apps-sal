((x1, y1), (x2, y2)) = ((1.52, 9.45), (1.83, 10.67))


def starting_mark(height):
    return round((height - x1) / (x2 - x1) * (y2 - y1) + y1, 2)
