def bar_triang(pointA, pointB, pointC):
    [xa, ya] = pointA
    [xb, yb] = pointB
    [xc, yc] = pointC
    return [round((xa + xb + xc) / 3, 4), round((ya + yb + yc) / 3, 4)]
