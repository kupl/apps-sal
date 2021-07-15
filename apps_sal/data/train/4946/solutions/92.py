def house_numbers_sum(inp):
    if 0 not in inp:
        return sum(inp)
    else:
        return sum(inp[:inp.index(0)])
