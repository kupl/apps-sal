def expression_matter(a, b, c):
    result = a * (b + c)
    new = a * b * c
    if new > result:
        result = new
    new = a + b * c
    if new > result:
        result = new
    new = (a + b) * c
    if new > result:
        result = new
    new = a + b + c
    if new > result:
        result = new
    return result
