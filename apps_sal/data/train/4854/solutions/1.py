def count_circles(circles, point):
    return sum(inside(circle_xyr(circle), point) for circle in circles)
    
def inside(xyr, pt):
    if xyr is None: return False
    x, y, r = xyr
    return dist(pt, (x, y)) <= r
    
def circle_xyr(pts):
    if len(pts) != 3: return None

    m1, c1 = perpbisector(pts[0], pts[1])
    m2, c2 = perpbisector(pts[0], pts[2])
    if m1 == m2: return None
    x, y = (c1, m2*c1 + c2) if m1 is None else (c2, m1*c2 + c1) if m2 is None else ((c2 - c1)/(m1 - m2), m1*(c2 - c1)/(m1 - m2) + c1)
    return x, y, dist(pts[0], (x, y))

def perpbisector(a, b):
    ax, ay = a
    bx, by = b
    mpx, mpy = (ax + bx) / 2.0, (ay + by) / 2.0
    if ax == bx: return 0, mpy
    if ay == by: return None, mpx
    m = (ax - bx) / float(by - ay)
    c = mpy - m * mpx
    return m, c
    
def dist(a, b):    
    return round(((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5, 8)
