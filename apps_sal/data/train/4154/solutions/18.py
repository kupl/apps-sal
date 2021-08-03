def is_triangle(a, b, c):
    sides = [a, b, c]
    max_side = max(sides)
    if sum(sides) - max_side > max_side:
        return True
    else:
        return False
