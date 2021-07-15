def expression_matter(a, b, c):
    op1 = (a + b) * c
    op2 = (a * b) * c
    op3 = (a * b * c)
    op4 = a * (b + c)
    op5 = (a + b + c)
    return max(op1, op2, op3, op4, op5)
