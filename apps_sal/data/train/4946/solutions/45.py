def house_numbers_sum(inp):
    output = 0
    for number in inp:
        if number == 0:
            break
        output += number
    
    return output
