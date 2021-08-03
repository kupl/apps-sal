def starting_mark(height):
    HEIGHT_1 = 1.52
    HEIGHT_2 = 1.83
    START_MARK_1 = 9.45
    START_MARK_2 = 10.67

    # y = k*x + m
    k = (START_MARK_2 - START_MARK_1) / (HEIGHT_2 - HEIGHT_1)
    m = START_MARK_1 - k * HEIGHT_1
    y = k * height + m

    return round(y, 2)
