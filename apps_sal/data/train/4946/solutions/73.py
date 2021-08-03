def house_numbers_sum(inp):
    tot = 0
    for x in inp:
        tot += x
        if x == 0:
            break
    return tot
