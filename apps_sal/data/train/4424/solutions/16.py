def expression_matter(a, b, c):
    expressions = [
        a * (b + c),
        a * b * c,
        a + b * c,
        (a + b) * c,
        a + b + c
    ]
    max_value = 0
    for expression in expressions:
        value = expression
        if value > max_value:
            max_value = value
    return max_value
