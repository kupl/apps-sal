def count_circles(list_of_circles, point):
    c = 0
    for circle in list_of_circles:
        (x1, y1), (x2, y2), (x3, y3) = circle[0], circle[1], circle[2]
        x = (x2**2 + y2**2 - x1**2 - y1**2) * (y3 - y1) - (x3**2 + y3**2 - x1**2 - y1**2) * (y2 - y1)
        x /= 2.0 * ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
        y = (x2**2 + y2**2 - x1**2 - y1**2) * (y3 - y1) - 2 * (x2 - x1) * (y3 - y1) * x
        y /= 2.0 * (y2 - y1) * (y3 - y1)
        r = ((x1 - x)**2 + (y1 - y)**2)**0.5
        d = ((x - point[0])**2 + (y - point[1])**2)**0.5
        if d <= r or abs(r - d) <= 10e-10:
            c += 1
    return c
