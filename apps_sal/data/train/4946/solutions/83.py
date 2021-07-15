def house_numbers_sum(inp):
    s = 0
    for x in inp:
        if x == 0:
            return s
        else:
            s += x
    return s
