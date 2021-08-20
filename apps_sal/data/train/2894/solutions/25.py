def triple_trouble(one, two, three):
    four = ''
    for x in range(len(one)):
        four += one[x] + two[x] + three[x]
    return four
