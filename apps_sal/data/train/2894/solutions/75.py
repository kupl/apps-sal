def triple_trouble(one, two, three):
    x = []
    for i in range(len(one)):
        x.append(one[i])
        x.append(two[i])
        x.append(three[i])
    return ''.join(x)
