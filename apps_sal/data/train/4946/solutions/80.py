def house_numbers_sum(inp):
    s = 0
    for x in inp:
        s = s + x
        if x == 0:
            return s
