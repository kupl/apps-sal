def house_numbers_sum(inp):
    count = 0
    for item in inp:
        count += item
        if item == 0:
            break
    return count
