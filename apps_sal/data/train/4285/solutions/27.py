def find_slope(points):
    x1, y1, x2, y2 = points
    try:
        slope = (y2 - y1) / (x2 - x1)
        return str(round(slope))
    except:
        return 'undefined'
