def house_numbers_sum(inp):
    x = []
    if inp[0] == 0:
        return 0
    else:
        for i in inp:
            if i != 0:
                x.append(i)
                continue
            elif i == 0:
                break
        return sum(x)
