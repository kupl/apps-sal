def isMultiple(a, b, n):
    frac_part = int(10.0 * (a / b - a // b) + 0.5) % 10
    return frac_part != 0 and frac_part % n == 0
