def bar_triang(pointA, pointB, pointC):  # points A, B and C will never be aligned
    xO = round(sum(x[0] for x in [pointA, pointB, pointC]) / 3, 4)
    yO = round(sum(y[1] for y in [pointA, pointB, pointC]) / 3, 4)
    return [xO, yO]  # coordinates of the barycenter expressed up to four decimals
    # (rounded result)
