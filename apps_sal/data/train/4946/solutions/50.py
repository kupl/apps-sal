def house_numbers_sum(inp):
    sm, i = 0, 0
    while inp[i] != 0:
        sm += inp[i]
        i += 1
    return sm
