def expression_matter(a, b, c):
    if a == 1 and b != 1 and c != 1:
        return (a + b) * c
    if a != 1 and b == 1 and c != 1 and (a > c or a == c):
        return a * (b + c)
    if a != 1 and b == 1 and c != 1 and a < c:
        return (a + b) * c
    if a != 1 and b != 1 and c == 1:
        return a * (b + c)
    if a > 1 and b > 1 and c > 1:
        return a * b * c
    if a > 1 and b == 1 and c == 1:
        return a * (b + c)
    if a == 1 and b == 1 and c > 1:
        return (a + b) * c
    else:
        return a + b + c
    

