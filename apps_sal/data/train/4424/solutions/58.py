def expression_matter(a, b, c):
    sample1 = a + b + c
    sample2 = a * b * c
    sample3 = (a + b) * c
    sample4 = a * (b + c)
    return max(sample1, sample2, sample3, sample4)
