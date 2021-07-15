import math
def ellipse_contains_point(f0, f1, l, p): 
    def dist2d(p1, p2):
        return math.sqrt((p2['x'] - p1['x']) ** 2 + (p2['y'] - p1['y']) ** 2)
    return dist2d(p,f0) + dist2d(p,f1) <= l
