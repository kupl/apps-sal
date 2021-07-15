def house_numbers_sum(inp):
    if (inp == [] or inp[0] == 0):
        return 0
    return house_numbers_sum(inp[1:]) + inp[0]
