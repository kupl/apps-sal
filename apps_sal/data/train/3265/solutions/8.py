def mult_triangle(n):
    s = n * (n + 1) // 2
    s *= s
    d = (n + 1) // 2
    d *= d
    return [s, s - d * d, d * d]
