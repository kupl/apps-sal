def house_numbers_sum(inp):
    total = 0
    for house_num in inp:
        if house_num == 0:
            return total
        else:
            total += house_num
