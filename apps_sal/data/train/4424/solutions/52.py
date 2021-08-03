def expression_matter(a, b, c):
    if (a * (b + c) >= (a + b) * c) and (a * (b + c) >= a + b + c) and (a * (b + c) >= a * b * c):
        return a * (b + c)
    if ((a + b) * c >= a * (b + c)) and ((a + b) * c) >= (a + b + c) and ((a + b) * c) >= (a * b * c):
        return (a + b) * c
    if (a * b * c >= (a + b) * c) and (a * b * c >= a + b + c) and (a * b * c >= a * (b + c)):
        return a * b * c
    else:
        return a + b + c
