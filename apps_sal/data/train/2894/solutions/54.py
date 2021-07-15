def triple_trouble(one, two, three):
    res = ''
    a = one, two, three
    for i in range(len(one)):
        res += one[i]
        res += two[i]
        res += three[i]
    return res
