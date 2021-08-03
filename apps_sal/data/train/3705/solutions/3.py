def heron(*sides):
    s = sum(sides) / 2
    a, b, c = sides
    return round((s * (s - a) * (s - b) * (s - c))**0.5, 2)
