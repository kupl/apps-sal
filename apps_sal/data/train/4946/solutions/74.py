def house_numbers_sum(inp):
    tab = []
    for x in inp:
        if x != 0:
            tab.append(x)
        else:
            break
    return (sum(tab))
