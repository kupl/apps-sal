def expression_matter(a, b, c):
    maxValue = a * b * c
    if a * (b+c) > maxValue:
        maxValue = a * (b+c)
    if a + b + c > maxValue:
        maxValue = a + b + c
    if a + b * c > maxValue:
        maxValue = a + b * c
    if (a+b) * c > maxValue:
        maxValue = (a+b) * c
    return maxValue
