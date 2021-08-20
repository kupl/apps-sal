def expression_matter(a, b, c):
    print(a, b, c)
    arr = []
    d = a * b * c
    arr.append(d)
    e = (a + b) * c
    arr.append(e)
    f = a * (b + c)
    arr.append(f)
    g = a + b * c
    arr.append(g)
    h = a * b + c
    arr.append(h)
    i = a + b + c
    arr.append(i)
    return max(arr)
