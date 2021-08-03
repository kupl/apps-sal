def expression_matter(a, b, c):
    h1 = a + b + c
    h2 = a * b * c
    h3 = a + b * c
    h4 = a * b + c
    h5 = (a + b) * c
    h6 = a + (b * c)
    h7 = a * (b + c)
    return max(h1, h2, h3, h4, h5, h6, h7)
