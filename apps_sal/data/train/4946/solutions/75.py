def house_numbers_sum(inp):
    index = inp.index(0)
    return sum([a for a in inp[:index]])
