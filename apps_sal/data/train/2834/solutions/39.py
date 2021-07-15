def symmetric_point(p, q):
    
    #Find the difference between midpoint Q and initial point P
    #Add this difference to the midpoint to find end point P1
    #Compatible with negative points
    
    p1x = q[0]+(q[0]-p[0])
    p1y = q[1]+(q[1]-p[1])
    return [p1x,p1y]
