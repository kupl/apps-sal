def house_numbers_sum(inp):
    lst = []
    for i in inp:
        if i == 0:
            break
        else:
            lst.append(i)
    return sum(lst)
