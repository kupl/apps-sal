def expression_matter(a, b, c):
    if a == 1 and b != 1 and c != 1:
        return (a + b) * c
    elif a != 1 and b == 1 and c != 1:
        if (a + b) * c > a * (b + c):
            return (a + b) * c
        else:
            return a * (b + c)
    elif a != 1 and b != 1 and c == 1:
        return a * (b + c)
    elif a == 1 and b == 1 and c == 1:
        return a + b + c
    elif (a == 1 and b == 1 and c != 1):
        return (a + b) * c
    elif (a == 1 and b != 1 and c == 1):
        return a + b + c
    elif (a != 1 and b == 1 and c == 1):
        return a * (b + c)
    else:
        return a * b * c
