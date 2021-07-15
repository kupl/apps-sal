from itertools import takewhile

def house_numbers_sum(inp):
    return sum(takewhile((0).__ne__, inp))
