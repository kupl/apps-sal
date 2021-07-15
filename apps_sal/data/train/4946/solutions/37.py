def house_numbers_sum(inp):
    res = []
    for num in inp:
        if num == 0:
            break
        else:
            res.append(num)
    return sum(res)
