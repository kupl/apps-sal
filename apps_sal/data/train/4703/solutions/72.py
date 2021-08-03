def bar_triang(pointA, pointB, pointC):  # points A, B and C will never be aligned
    x0 = (float(pointA[0]) + float(pointB[0]) + float(pointC[0])) / 3
    y0 = (float(pointA[1]) + float(pointB[1]) + float(pointC[1])) / 3
    return [round(x0, 4), round(y0, 4)]  # coordinates of the barycenter expressed up to four decimals
    # (rounded result)
