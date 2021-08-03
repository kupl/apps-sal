def ellipse_contains_point(f0, f1, l, p):
    return ((p['x'] - f0['x'])**2 + (p['y'] - f0['y'])**2)**.5 + ((p['x'] - f1['x'])**2 + (p['y'] - f1['y'])**2)**.5 <= l
