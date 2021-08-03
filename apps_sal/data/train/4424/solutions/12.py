def expression_matter(a, b, c):
    largest_number = 0
    rlt1 = a * (b + c)
    rlt2 = a * b * c
    rlt3 = a + b * c
    rlt4 = (a + b) * c
    rlt5 = a + b + c
    rlt6 = a * b + c
    list = [rlt1, rlt2, rlt3, rlt4, rlt5, rlt6]

    for li in list:
        if li > largest_number:
            largest_number = li

    return largest_number
