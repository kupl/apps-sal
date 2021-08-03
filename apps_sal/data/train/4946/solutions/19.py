def house_numbers_sum(inp):
    suma = []
    for i in range(0, len(inp) + 1):
        if inp[i] == 0:
            break
        else:
            suma.append(inp[i])
    return sum(suma)
