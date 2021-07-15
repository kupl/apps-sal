def expression_matter(a, b, c):
    value_1 = a+b+c
    value_2 = a*b*c
    value_3 = a*(b+c)
    value_4 = (a+b)*c
    value_5 = a*b+c
    value_6 = a+b*c
    empty_list = []
    empty_list.append(value_1)
    empty_list.append(value_2)
    empty_list.append(value_3)
    empty_list.append(value_4)
    empty_list.append(value_5)
    empty_list.append(value_6)
    return max(empty_list)
