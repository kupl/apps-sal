def repeater(string, n):
    z = []
    for x in range(n):
        z.append(string)

    makestr = ''.join(map(str, z))
    return makestr
