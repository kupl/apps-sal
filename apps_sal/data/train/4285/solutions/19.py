def find_slope(points):
    
    x = points[2]-points[0]
    return 'undefined' if x == 0 else str((points[3]-points[1])//(points[2]-points[0]))

