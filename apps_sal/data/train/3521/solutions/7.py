def on_line(points):

    def slope_intercept(p1, p2):
        slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
        intercept = p1[1] - slope * p1[0]
        return (slope, intercept)
    if len(points) == 0 or isinstance(points[0], int):
        return True
    for (p1, p2) in zip(points, points[1:]):
        if p1[0] == p2[0] or p1[1] == p2[1]:
            continue
        else:
            (s, i) = slope_intercept(p1, p2)
            try:
                if abs(s - slope) > 1e-08 or abs(i - intercept) > 1e-06:
                    return False
            except:
                pass
            (slope, intercept) = (s, i)
    return True
