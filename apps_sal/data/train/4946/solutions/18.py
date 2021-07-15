def house_numbers_sum(inp):
    total = 0
    for num in inp:
        if num == 0:
            break
        else: 
            total +=num
    return total

