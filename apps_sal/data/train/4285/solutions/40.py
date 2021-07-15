def find_slope(points):
    if points[2]==points[0]:
        return 'undefined'
    else:
        return '0' if points[1]==points[3] else str((points[3]-points[1])//(points[2]-points[0]))


