def find_slope(points):
    x1 = points[0]
    x2 = points[2]
    y1 = points[1]
    y2 = points[3]

    x3 = (x2 - x1)
    y3 = (y2 - y1)

    if(x3 == 0):
        return 'undefined'
    else:
        return f'{y3 // x3}'
