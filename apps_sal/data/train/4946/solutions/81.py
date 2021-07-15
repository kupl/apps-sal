def house_numbers_sum(inp):
    total = 0
    for i in range(len(inp)):
        if inp[i] == 0:
            break
        else:
            total += inp[i]
    return total
