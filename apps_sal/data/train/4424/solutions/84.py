def expression_matter(a, b, c):
    arr = []
    arr.append(a + b + c)
    arr.append(a + b * c)
    arr.append(a * b + c)
    arr.append(a * (b + c))
    arr.append((a + b) * c)
    arr.append(a * b * c)
    return max(arr)
