def triple_trouble(one, two, three):
    tot = ''
    for x in range(len(one)):
        tot += one[x] + two[x] + three[x]
    return tot
