def house_numbers_sum(inp):
    return sum(inp[:inp.index(0)+1]) if inp[0] !=0 else 0
