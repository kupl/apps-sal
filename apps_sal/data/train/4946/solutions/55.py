def house_numbers_sum(inp):
    result = 0
    for n in inp:
        if n == 0:
            return result
        else:
            result += n
    return result
