def triple_trouble(one, two, three):
    str = ''
    for n in range(len(one)):
        str += one[n] + two[n] + three[n]
    return str
