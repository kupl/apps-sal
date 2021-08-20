def find_slope(points):
    lower = points[2] - points[0]
    upper = points[3] - points[1]
    if upper == 0 and lower == 0:
        return 'undefined'
    elif upper == 0:
        return '0'
    elif lower == 0:
        return 'undefined'
    else:
        return str(int(upper / lower))
