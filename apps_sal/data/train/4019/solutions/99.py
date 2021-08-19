def max_multiple(divisor, bound):
    my_num = 0
    for item in range(1, bound + 1):
        if item % divisor == 0:
            my_num = item
    return my_num
