def expression_matter(a, b, c):
    no_1 = a * (b + c)
    no_2 = a + b + c
    no_3 = a * b * c
    no_4 = (a + b) * c
    if no_3 > no_1 and no_3 > no_2 and no_3 > no_4:
        return no_3
    if no_4 > no_1 and no_4 > no_2:
        return no_4
    if no_2 > no_1:
        return no_2
    else:
        return no_1
