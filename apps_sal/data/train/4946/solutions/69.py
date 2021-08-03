def house_numbers_sum(inp):
    i = 0
    out = 0
    while inp[i] != 0:
        out += inp[i]
        i += 1
    return out
