def house_numbers_sum(inp):
    x = inp.index(0)
    return sum((i for i in inp[:x]))
