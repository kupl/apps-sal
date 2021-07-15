from math import pi as PI

def sort_by_area(lst):
    return sorted(lst, key=lambda d: d[0] * d[1] if isinstance(d, tuple) else PI * d * d)   
