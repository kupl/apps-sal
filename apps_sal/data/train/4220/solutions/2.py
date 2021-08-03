def equable_triangle(a, b, c):
    return (a + b + c) * 16 == (a + b - c) * (b + c - a) * (c + a - b)
