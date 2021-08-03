def find_slope(points):
    a = points[0]
    b = points[1]
    c = points[2]
    d = points[3]

    if c - a == 0:
        return 'undefined'
    else:
        return str(int((d - b) / (c - a)))
