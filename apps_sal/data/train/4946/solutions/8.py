def house_numbers_sum(inp):
    total = 0
    for num in inp:
        if num != 0:
            total += num
        else:
            break
    return total
