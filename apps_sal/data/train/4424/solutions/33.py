def expression_matter(a, b, c):
    largest = 0
    if a + b + c > largest:
        largest = a + b + c
    if a + b * c > largest:
        largest = a + b * c
    if a * b + c > largest:
        largest = a * b + c
    if a * b * c > largest:
        largest = a * b * c
    if (a + b) * c > largest:
        largest = (a + b) * c
    if a * (b + c) > largest:
        largest = a * (b + c)
    return largest
