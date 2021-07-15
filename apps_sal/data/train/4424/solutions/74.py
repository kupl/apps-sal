def expression_matter(a, b, c):
    res_1 = a + b + c
    res_2 = a * b * c
    res_3 = a + b * c
    res_4 = a * b + c
    res_5 = (a + b) * c
    res_6 = a * (b + c)
    return max(res_1, res_2, res_3, res_4, res_5, res_6)

