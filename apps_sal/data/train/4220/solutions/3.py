def equable_triangle(a, b, c):
    p = a + b + c
    d = p / 2
    return (d * (d - a) * (d - b) * (d - c)) ** 0.5 == p
