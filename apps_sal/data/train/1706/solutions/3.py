def rectangle_rotation(a, b):
    b1 = b // (2**(1 / 2)) + 1
    a1 = a // (2**(1 / 2)) + 1
    c = a1 * b1 + (a1 - 1) * (b1 - 1)
    return c if c % 2 == 1 else c - 1
