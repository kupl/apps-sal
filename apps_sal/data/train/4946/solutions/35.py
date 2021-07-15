def house_numbers_sum(inp):
    sum = i = 0
    while i < len(inp) and inp[i] != 0:
        sum += inp[i]
        i += 1
    return sum
