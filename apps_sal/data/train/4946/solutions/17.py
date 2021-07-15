def house_numbers_sum(inp):
    list = []
    for i in range(0, len(inp)+1):
        if inp[i] == 0:
            break
        else:
            list.append(inp[i])
    return sum(list)
        
        
        

