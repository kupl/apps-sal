def house_numbers_sum(inp):
    my_l = []
    for num in inp:
        if num != 0:
            my_l.append(num)
        else:
            break
    return sum(my_l)
