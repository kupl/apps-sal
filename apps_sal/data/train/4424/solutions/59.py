def expression_matter(a, b, c):

    result_1 = (a + b) * c
    result_2 = a * (b + c)
    result_3 = (a + b) * c
    result_4 = a * b * c
    result_5 = a + b + c


    if result_1 >= result_2 and result_1 >= result_3 and result_1 >= result_4 and result_1 >= result_5:
        return result_1
    elif result_2 >= result_1 and result_2 >= result_3 and result_2 >= result_4 and result_2 >= result_5:
        return result_2
    elif result_3 >= result_1 and result_3 >= result_2 and result_3 >= result_4 and result_3 >= result_5:
        return result_3
    elif result_4 >= result_1 and result_4 >= result_2 and result_4 >= result_3 and result_4 >= result_5:
        return result_4
    elif result_5 >= result_1 and result_5 >= result_2 and result_5 >= result_3 and result_5 >= result_4:
        return result_5
