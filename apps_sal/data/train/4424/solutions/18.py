def expression_matter(a, b, c):
    val1 = a * b * c
    val2 = (a + b) * c
    val3 = a * (b + c)
    val4 = a + b * c
    val5 = a * b + c
    val6 = a + b + c
    a = [val1, val2, val3, val4, val5, val6]
    return max(a)
