def expression_matter(a, b, c):
    a = [a * (b + c), a * b * c, (a + b) * c, a + b + c]
    return max(a)
