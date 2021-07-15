def expression_matter(a, b, c):
    x = []
    x.append(a * (b + c))
    x.append(a * b * c)
    x.append(a + b * c)
    x.append((a + b) * c)
    x.append(a + b + c)
    return max(x)
