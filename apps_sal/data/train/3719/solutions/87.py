def starting_mark(height):
    # 10.67 = 1.83*a + b
    #  9.45 = 1.52*a + b
    # ------------------ -
    #  1.22 = 0.31*a
    # a = 3.93548
    a = 1.22 / 0.31
    b = 9.45-1.52*a
    return round(a*height + b,2)
