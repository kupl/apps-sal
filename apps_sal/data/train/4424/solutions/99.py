def expression_matter(a, b, c):
    print(a, b, c)
    x = (a + b) * c
    y = a * (b + c)
    z = a + b + c
    w = a * b * c
    v = a + b * c
    v1 = a * b + c
    return max(x, y, z, w, v, v1)
