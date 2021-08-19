def expression_matter(a, b, c):
    s = a + b + c
    m = a * b * c
    n = (a + b) * c
    o = a * (b + c)
    q = a * b + c
    r = a + b * c
    return max(s, m, n, o, q, r)
