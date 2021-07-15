def house_numbers_sum(inp):
    total = 0
    for x in inp:
        if x != 0:
            total = total + x
        else:
            return total

