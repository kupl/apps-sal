def expression_matter(a, b, c):
    s = []
    s.append(a * b * c)
    s.append(a + b + c)
    s.append(a + b * c)
    s.append((a + b) * c)
    s.append(a * b + c)
    s.append(a * (b + c))
    return max(s)
