def starting_mark(height):
    slp = (10.67 - 9.45) / (1.83 - 1.52)
    cst = 9.45 - slp * 1.52
    return round( slp * height + cst, 2 )
