def area(d, l):
    return round(l * (d**2 - l**2)**0.5, 2) if d > l else "Not a rectangle"
