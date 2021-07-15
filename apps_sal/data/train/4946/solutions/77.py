def house_numbers_sum(inp):
    result = 0
    for i in inp:
        if i == 0:
            break
        else:
            result += i
    return result
