def on_line(points):
    points = list(set(points))
    cross_product = lambda a, b, c: a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1])
    return all(cross_product(p, *points[:2]) == 0 for p in points[2:])
