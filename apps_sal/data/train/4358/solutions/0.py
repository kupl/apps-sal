def dist(p1, p2): return ((p1['x'] - p2['x'])**2 + (p1['y'] - p2['y'])**2)**0.5


def ellipse_contains_point(f0, f1, l, p): return dist(p, f0) + dist(p, f1) <= l
