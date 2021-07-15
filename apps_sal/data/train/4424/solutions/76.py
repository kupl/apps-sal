def expression_matter(a, b, c):
    answer_1 = a * (b + c)
    answer_2 = a * b * c
    answer_3 = a + b * c
    answer_4 = (a + b) * c
    answer_5 = a + b + c
    return max(answer_1, answer_2, answer_3, answer_4, answer_5)
