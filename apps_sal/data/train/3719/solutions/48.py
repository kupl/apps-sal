def starting_mark(height):
    if height <= 1.52:
        res = 9.45 - ((1.52 - height) * (10.67 - 9.45) / (1.83 - 1.52))
    elif 1.52 < height <= 1.83:
        res = 10.67 - ((1.83 - height) * (10.67 - 9.45) / (1.83 - 1.52))
    else:
        res = 10.67 + ((height - 1.83) * (10.67 - 9.45) / (1.83 - 1.52))
    return round(res, 2)
