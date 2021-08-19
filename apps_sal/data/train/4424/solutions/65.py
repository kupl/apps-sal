def expression_matter(a, b, c):
    result1 = a * (b + c)
    result2 = a * b * c
    result3 = a + b * c
    result4 = (a + b) * c
    result5 = a + b + c
    return max(result1, result2, result3, result4, result5)
