def area(d, l):
    return round(l * ((d * d - l * l) ** 0.5), 2) if d > l else "Not a rectangle"
