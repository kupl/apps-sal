def on_line(points):
    points = list(set(points))
    def cross_product(a, b, c): return a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])
    return all(cross_product(p, *points[:2]) == 0 for p in points[2:])
