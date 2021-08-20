def ellipse_contains_point(f0, f1, l, p):
    (x1, x2, y1, y2) = (f0['x'] - p['x'], f1['x'] - p['x'], f0['y'] - p['y'], f1['y'] - p['y'])
    d1 = (x1 ** 2 + y1 ** 2) ** 0.5
    d2 = (x2 ** 2 + y2 ** 2) ** 0.5
    return d2 + d1 <= l
