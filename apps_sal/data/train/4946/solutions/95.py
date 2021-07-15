def house_numbers_sum(inp):
    for idk, i in enumerate(inp): 
        if i == 0:
            return sum(inp[:idk])
