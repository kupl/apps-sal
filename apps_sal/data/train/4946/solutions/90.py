def house_numbers_sum(inp):
    s = 0
    for i in inp:
        if i != 0:
            s += i
        else:
            return s
