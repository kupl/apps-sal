def house_numbers_sum(inp):
    sum = 0
    for x in inp:
        if x != 0:
            sum += x
        else:
            break
    return sum
