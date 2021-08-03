def hex_to_dec(s):
    n = 0
    p = 1
    for x in s[::-1]:
        if x == "a":
            n += 10 * p
        elif x == "b":
            n += 11 * p
        elif x == "c":
            n += 12 * p
        elif x == "d":
            n += 13 * p
        elif x == "e":
            n += 14 * p
        elif x == "f":
            n += 15 * p
        else:
            n += int(x) * p
        p *= 16
    return n
