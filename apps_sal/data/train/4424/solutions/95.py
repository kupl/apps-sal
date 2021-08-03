def expression_matter(a, b, c):
    v1 = a + b + c
    v2 = (a + b) * c
    v3 = a * (b + c)
    v4 = a * b * c
    return max(v1, v2, v3, v4)
