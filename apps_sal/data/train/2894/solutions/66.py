def triple_trouble(one, two, three):
    output = ''
    for x in range(len(one)):
        output += one[x]
        output += two[x]
        output += three[x]
    return output
