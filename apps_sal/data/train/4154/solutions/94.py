def is_triangle(a, b, c):
    sides = [a, b, c]
    a = max(sides)
    sides.remove(a)
    if sum(sides) > a:
        return True
    return False
