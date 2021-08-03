def ellipse_contains_point(f0, f1, l, p):
    x1, x2, y1, y2 = f0['x'], f1['x'], f0['y'], f1['y']
    c = (((x1 - x2)**2 + (y1 - y2)**2)**.5) / 2
    h, k = (x1 + x2) / 2, (y1 + y2) / 2
    a = c + (l - 2 * c) / 2
    b = ((l / 2)**2 - c)**.5
    return ((p['x'] - h)**2) / a**2 + ((p['y'] - k)**2) / b**2 <= 1 and c < l / 2.
