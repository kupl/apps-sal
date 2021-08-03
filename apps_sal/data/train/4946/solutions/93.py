def house_numbers_sum(inp):
    hardstop = inp.index(0)

    house_sum = 0

    for i in range(0, hardstop):
        house_sum += inp[i]

    return house_sum
