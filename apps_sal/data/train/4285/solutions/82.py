def find_slope(points):
    delta_x = points[0] - points[2]
    delta_y = points[1] - points[3]
    
    if delta_x == 0:
        return 'undefined'
    else:
        return str(int(delta_y / delta_x))    
