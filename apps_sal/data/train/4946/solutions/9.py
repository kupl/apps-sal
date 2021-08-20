def house_numbers_sum(inp):
    return sum((next(iter([])) if i == 0 else i for i in inp))
