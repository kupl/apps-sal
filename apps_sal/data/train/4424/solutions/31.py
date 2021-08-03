def expression_matter(a, b, c):
    n1 = a + b + c
    n2 = a * b * c
    n3 = a * (b + c)
    n4 = (a + b) * c
    n5 = a + (b * c)
    n6 = (a * b) + c
    return max(n1, n2, n3, n4, n5, n6)
