def expression_matter(a, b, c):
    list_exp = []
    list_exp.append(a * b + c)
    list_exp.append(a + b * c)
    list_exp.append((a + b) * c)
    list_exp.append(a * (b + c))
    list_exp.append(a + b + c)
    list_exp.append(a * b * c)
    list_exp.append(a + b + c)
    return max(list_exp)
