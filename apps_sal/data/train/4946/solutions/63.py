def house_numbers_sum(inp):
    i = 0
    ln = len(inp)
    res = 0
    while i < ln and inp[i] != 0:
        res += inp[i]
        i += 1
        
    return res
