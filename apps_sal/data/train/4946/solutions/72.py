def house_numbers_sum(inp):
    a = 0
    for n in inp:
        if n == 0:
            return a
        a += n
    return a
