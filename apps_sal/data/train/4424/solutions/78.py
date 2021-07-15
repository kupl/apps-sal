def expression_matter(a, b, c):
    x = a * (b + c)
    y = a * b * c
    z = a + b * c
    i = (a + b) * c
    m = a + b + c
    
    arr = [x, y, z, i, m]
    arr.sort()
    return max(arr)
