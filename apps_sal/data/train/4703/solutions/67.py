def bar_triang(pointA, pointB, pointC):  # points A, B and C will never be aligned
    xa, ya, xb, yb, xc, yc = pointA + pointB + pointC
    return [round((xa + xb + xc) / 3, 4), round((ya + yb + yc) / 3, 4)]
