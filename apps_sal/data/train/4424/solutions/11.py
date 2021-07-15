def expression_matter(a, b, c):
    if 1 not in [a, b, c]:
        return a * b * c
    elif a == 1 and c == 1:
        return a + b + c
    elif a == 1 or (b == 1 and a < c):
        return (a + b) * c
    else:
        return a * (b + c)
