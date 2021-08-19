def hex_to_dec(s):
    hex = '0123456789abcdef'
    deci = 0
    place = 0
    for x in reversed(s):
        if place == 0:
            deci += hex.index(x)
        else:
            deci += hex.index(x) * 16 ** place
        place += 1
    return deci
