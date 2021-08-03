def number(bus):
    c = 0
    for j in bus:
        c += j[0] - j[1]
    return c
