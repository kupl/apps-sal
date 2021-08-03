def expression_matter(a, b, c):
    li = []
    li.append(a * b * c)
    li.append(a + b + c)
    li.append(a + (b * c))
    li.append(a * (b + c))
    li.append((a + b) * c)
    li.append((a * b) + c)
    return max(li)
