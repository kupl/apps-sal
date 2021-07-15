def house_numbers_sum(inp):
    a = []
    for x in inp:
        if x != 0:
            a.append(x)
        else:
            break
    return sum(a)
