def bar_triang(pointA, pointB, pointC):  # points A, B and C will never be aligned

    xa, ya = pointA
    xb, yb = pointB
    xc, yc = pointC

    xO = round((xa + xb + xc) / 3, 4)
    yO = round((ya + yb + yc) / 3, 4)

    return [xO, yO]  # coordinates of the barycenter expressed up to four decimals
    # (rounded result)
