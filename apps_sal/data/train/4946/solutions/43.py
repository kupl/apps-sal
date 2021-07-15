def house_numbers_sum(inp):
    counter = 0
    for x in inp:
        counter += x
        if x == 0:
            break
    return counter
