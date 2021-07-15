def equable_triangle(a, b, c):
    p = a + b + c
    ph = p / 2
    return p * p == ph * (ph - a) * (ph - b) * (ph - c)
