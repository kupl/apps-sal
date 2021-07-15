def house_numbers_sum(inp):
    return sum(__import__('itertools').takewhile(bool, inp))
