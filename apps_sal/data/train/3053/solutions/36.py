def close_compare(a, b, margin=0):  # margin = 0  -optional element
    difference = abs(a - b)  # difference between a and b

    if margin >= difference:  # a is close to b
        return 0
    elif a > b:  # a is higher
        return 1
    elif a < b:  # a is lower
        return -1

    pass
