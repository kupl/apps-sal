def points(a):
    return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))
