def max_product(a):
    first_max = 0
    second_max = 0
    for x in a:
        if x > first_max:
            second_max = first_max
            first_max = x
        elif x > second_max:
            second_max = x
    return first_max * second_max
