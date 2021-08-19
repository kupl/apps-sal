def expression_matter(a, b, c):
    x = a + b + c
    y = (a + b) * c
    z = a * (b + c)
    w = a * b * c

    lis = [x, y, z, w]
    ans = max(lis)
    return ans  # highest achievable result
