def house_numbers_sum(inp):
    res = 0
    for num in inp:
        if num == 0:
            return res
        res+=num
    return -1

