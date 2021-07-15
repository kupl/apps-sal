def expression_matter(a, b, c):
    a1 = (a + b) * c
    a2 = a * b * c
    a3 = a * (b + c)
    a4 = a + b * c
    a5 = a + b + c
    return max(a1, a2, a3, a4, a5)
