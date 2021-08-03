def triple_trouble(one, two, three):
    i = 0
    list123 = []
    while i < len(one):
        list123.append(one[i])
        list123.append(two[i])
        list123.append(three[i])
        i += 1
    return ''.join(list123)
