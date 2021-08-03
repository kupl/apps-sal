def house_numbers_sum(inp):
    ind = inp.index(0)
    s = 0
    for i in range(0, ind):
        s = s + inp[i]
    return s
