def is_triangle(a, b, c):
    if any(side <= 0 for side in (a, b, c)):
        return False
    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        return False
    return True
