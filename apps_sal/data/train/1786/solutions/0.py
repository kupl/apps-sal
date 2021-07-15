import numpy as np

def slope(p1, p2):
    dx, dy = vectorize(p1, p2)
    return dy/dx if dx else float("inf")

def vectorize(p1, p2):         return [b-a for a,b in zip(p1, p2)]
def getArea  (p1, p2, p3):     return np.cross(vectorize(p1, p2), vectorize(p1, p3)) / 2
def isConcave(p1, pivot, p2):  return getArea(pivot, p1, p2) >= 0

def convex_hull_area(points):
    if len(points) < 3: return 0
    
    Z = min(points)                                                                      # Leftmost point in the graph (lowest if several ones at the same x)
    q = sorted( (pt for pt in points if pt != Z),
                key = lambda pt: (-slope(pt, Z), -np.linalg.norm(vectorize(Z, pt))))     # sorted points accordingly to the slope of the line formed by "pt" and "Z" (in reversed order)
    
    hull = [Z, q.pop()]                                                                  # Construct the convex hull (Graham Scan)
    while q:
        pt = q.pop()
        while len(hull) > 1 and isConcave(hull[-2], hull[-1], pt):
            hull.pop()
        hull.append(pt)
    
    area = sum( getArea(Z, hull[i], hull[i+1]) for i in range(1, len(hull)-1) )          # Calculate area of the hull by adding the area of all the triangles formed by 2 consecutive points in the hull and having Z as summit
    return round(area, 2)
