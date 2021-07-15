def bar_triang(pointA, pointB, pointC):
    xA, yA = pointA
    xB, yB = pointB
    xC, yC = pointC
    
    x0 = (xA + xB + xC) / 3
    y0 = (yA + yB + yC) / 3    
    
    return [round(x0, 4), round(y0, 4)]
