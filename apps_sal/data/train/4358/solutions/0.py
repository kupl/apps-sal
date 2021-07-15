dist = lambda p1, p2: ((p1['x']-p2['x'])**2+(p1['y']-p2['y'])**2)**0.5
ellipse_contains_point = lambda f0, f1, l, p : dist(p, f0)+dist(p, f1)<=l
