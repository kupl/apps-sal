def house_numbers_sum(inp):
    a = []
    sum = 0
    for i in inp:
        a.append(i)
        if i == 0:
            break
    for i in a:
        sum = sum + i
    return sum

