def bar_triang(pointA, pointB, pointC):
    ax, ay = pointA
    bx, by = pointB
    cx, cy = pointC
    x0 = round((ax + bx + cx) / 3, 4)
    y0 = round((ay + by + cy) / 3, 4)
    return [x0, y0]
