import math
def ellipse_contains_point(f0, f1, l, p): 
    return (math.hypot(p['x'] - f0['x'],p['y'] - f0['y']) + math.hypot(p['x'] - f1['x'],p['y'] - f1['y'])) <= l
