def starting_mark(height):
    # define gradient for our equation
    m = (10.67 - 9.45) / (1.83 - 1.52)
    # define our y-intercept for our equation
    c = 10.67 - (m * 1.83)
    # plug height into our formula and return value
    return round(m * height + c, 2)
