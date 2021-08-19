def house_numbers_sum(inp):
    res = [0]
    for i in inp:
        if i == 0:
            break
        res.append(i)
    return sum(res)
