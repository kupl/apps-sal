def points(r):
    rr = r * r
    x = sum((int((rr - x * x) ** 0.5) for x in range(r)))
    return x * 4 + 1
