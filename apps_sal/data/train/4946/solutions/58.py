def house_numbers_sum(inp):
    s = 0
    for e in inp:
        if e != 0:
            s += e
        else:
            return s
