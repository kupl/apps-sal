def expression_matter(a, b, c):
    e1 = a * b * c
    e2 = a + b + c
    e3 = (a + b) * c
    e4 = a * (b + c)
    list = []
    list.append(e1)
    list.append(e2)
    list.append(e3)
    list.append(e4)
    return max(list)
