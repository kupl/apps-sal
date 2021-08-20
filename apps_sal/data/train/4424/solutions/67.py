def expression_matter(a, b, c):
    max = 0
    if max < a + b + c:
        max = a + b + c
    if max < a + b * c:
        max = a + b * c
    if max < a * b * c:
        max = a * b * c
    if max < a * b + c:
        max = a * b + c
    if max < a + b * c:
        max = a + b * c
    if max < (a + b) * c:
        max = (a + b) * c
    if max < a * (b + c):
        max = a * (b + c)
    if max < a * b + c:
        max = a * b + c
    return max
