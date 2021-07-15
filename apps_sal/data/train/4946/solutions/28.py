def house_numbers_sum(inp):
    res = 0
    for n in inp:
        if n == 0:
            break
        else:
            res += n
    return res
