def house_numbers_sum(inp):
    res = 0
    for i in inp:
        res += i
        if i == 0:
            return res
