def equable_triangle(a, b, c):
    s = (a + b + c) / 2.0
    A = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return A == s * 2
