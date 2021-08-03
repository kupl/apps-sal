def expression_matter(a, b, c):
    if a == 1:
        b += 1
    if c == 1:
        b += 1
    if b == 1:
        if a < c:
            a += 1
        else:
            c += 1
    return a * b * c
