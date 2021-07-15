def house_numbers_sum(inp):
    l = []
    for i in inp:
        if i == 0:
            break
        else:l.append(i)
    return sum(l)
