def roots(a, b, c):
    D = b**2 - 4 * a * c
    if D < 0:
        return None
    if D == 0:
        x = (-b + D**0.5) / (2 * a)
        return round(x * 2, 2)
    if D > 0:
        x1 = (-b + D**0.5) / (2 * a)
        x2 = (-b - D**0.5) / (2 * a)
        return round((x1 + x2), 2)
