def expression_matter(a, b, c):
    lst = []
    lst.append(a * (b + c))
    lst.append(a * b * c)
    lst.append(a + b + c)
    lst.append((a + b) * c)
    return max(lst)
