def house_numbers_sum(inp):
    zero_index = inp.index(0)
    total = 0
    
    for number in inp[:zero_index]:
        total += number
        
    return total
