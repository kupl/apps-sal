def house_numbers_sum(inp):
    if inp[0] == 0:
        return 0
    else:
        return sum(inp[:inp.index(0)])
