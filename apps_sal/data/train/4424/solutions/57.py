def expression_matter(a, b, c):
    f = a * (b + c)
    d = a * b * c
    s = a + b * c
    v = (a + b) * c
    return max(f, d, s, v, a + b + c)
