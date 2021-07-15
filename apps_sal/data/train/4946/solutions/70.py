def house_numbers_sum(inp):
    total = 0
    for i in inp:
        if i != 0:
            total += i
        else:
            return total
