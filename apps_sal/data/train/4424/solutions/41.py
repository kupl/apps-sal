def expression_matter(a, b, c):
    result = 0
    result = max(result, a * (b + c))
    result = max(result, a * b * c)
    result = max(result, a + b * c)
    result = max(result, (a + b) * c)
    result = max(result, a + b + c)
    return result
