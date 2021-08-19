def expression_matter(a, b, c):
    res = []
    res.append(a + b + c)
    res.append(a + (b + c))
    res.append(a * b * c)
    res.append(a * (b * c))
    res.append((a + b) * c)
    res.append(a + b * c)
    res.append(a * b + c)
    res.append(a * (b + c))
    return max(res)
