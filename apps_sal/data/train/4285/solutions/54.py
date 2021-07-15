def find_slope(points: list):
    try:
        x1, y1, x2, y2 = points
        return str((y2 - y1) // (x2 - x1))
    except:
        return 'undefined'
