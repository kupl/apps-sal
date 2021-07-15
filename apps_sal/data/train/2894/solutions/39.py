def triple_trouble(one, two, three):
    list = []
    for x in range(len(one)):
        list.extend((one[x],two[x],three[x]))
    return ''.join(list)


