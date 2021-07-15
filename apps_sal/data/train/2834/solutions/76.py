def symmetric_point(p, q):
    dist_x = q[0] - p[0]
    dist_y = q[1] - p[1]
    
    p1_x = q[0] + dist_x
    p2_x = q[1] + dist_y
    
    return [p1_x, p2_x]
