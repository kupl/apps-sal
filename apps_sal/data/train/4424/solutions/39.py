def expression_matter(a, b, c):
    calc = [a * (b + c), a * b * c, a + b * c, (a + b) * c, a + b + c]
    return max(calc)
