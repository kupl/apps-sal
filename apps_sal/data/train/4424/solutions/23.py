def expression_matter(a, b, c):

    list = []
    list.append(a * b * c)
    list.append(a * (b + c))
    list.append(a + b * c)
    list.append((a + b) * c)
    list.append(a * b + c)
    list.append(a + b + c)

    return max(list)


expression_matter(1, 1, 1)
