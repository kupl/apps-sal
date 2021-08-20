def house_numbers_sum(inp):
    r = 0
    for n in inp:
        r += n
        if n == 0:
            break
    return r
