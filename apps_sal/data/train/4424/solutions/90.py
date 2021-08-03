def expression_matter(a, b, c):
    x = [a + b + c, a * b * c, (a + b) * c, a * (b + c)]
    return max(x)
