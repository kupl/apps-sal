def starting_mark(height):
    # your code here
    # slope of line = (y2 - y1) / (x2 - x1)
    slope = (10.67 - 9.45) / (1.83 - 1.52)
    # substitute slope and one set of x,y to find the y-intercept C
    # y = mx + c -> c = y - mx
    c = 10.67 - (slope * 1.83)
    # for the given x, return mx + c, rounded off to 2 decimals
    return round(slope * height + c, 2)
