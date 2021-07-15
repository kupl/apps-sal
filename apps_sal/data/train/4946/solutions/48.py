def house_numbers_sum(inp):
    inp = inp[:inp.index(0)]
    return sum(inp) if inp else 0
