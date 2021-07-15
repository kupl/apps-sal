def expression_matter(a, b, c):
    result = 0
    if a + b + c > result: result = a + b + c
    if a + b * c > result: result = a + b * c
    if a * b + c > result: result = a * b + c
    if a * b * c > result: result = a * b * c
    if (a + b) * c > result: result = (a + b) * c
    if a * (b + c) > result: result = a * (b + c)
    return result
