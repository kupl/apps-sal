def bar_triang(pointA, pointB, pointC):  # points A, B and C will never be aligned
    # your code here
    ax, ay = pointA
    bx, by = pointB
    cx, cy = pointC
    x0 = round((ax + bx + cx) / 3, 4)
    y0 = round((ay + by + cy) / 3, 4)
    return [x0, y0]  # coordinates of the barycenter expressed up to four decimals
    # (rounded result)
