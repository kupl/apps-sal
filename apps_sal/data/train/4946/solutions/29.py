def house_numbers_sum(inp):
    total = 0
    for x in inp:
        if x == 0:
            return total
        else:
            total+=x
