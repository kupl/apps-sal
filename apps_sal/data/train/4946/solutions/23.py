def house_numbers_sum(inp):
    cool = []
    for i in inp:
        if i != 0:
            cool.append(i)
        else:
            break
    return sum(cool)
