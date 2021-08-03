def capitalize(s):
    x = 2
    z = 2
    string = ''
    string2 = ''

    for i, y in zip(s, s):
        if x % 2 == 0:
            string = string + i.upper()
            x += 1
        else:
            string = string + i
            x += 1

        if z % 2 != 0:
            string2 = string2 + i.upper()
            z += 1
        else:
            string2 = string2 + i
            z += 1

    return [string, string2]
