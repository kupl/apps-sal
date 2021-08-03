import statistics


def expression_matter(a, b, c):
    lis = []
    lis.append(a * b * c)
    lis.append((a + b) * c)
    lis.append(a + (b * c))
    lis.append(a + b + c)
    lis.append((a * b) + c)
    lis.append(a * (b + c))
    return max(lis)
