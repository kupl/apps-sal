def house_numbers_sum(inp):
    my_list = []
    for i in inp:
        if i == 0:
            break
        else:
            my_list.append(i)
    return sum(my_list)
