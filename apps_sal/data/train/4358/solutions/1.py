from math import hypot

def ellipse_contains_point(f0, f1, l, p): 
    d0 = hypot(f0["x"] - p["x"], f0["y"] - p["y"])
    d1 = hypot(f1["x"] - p["x"], f1["y"] - p["y"])
    return d0 + d1 <= l
