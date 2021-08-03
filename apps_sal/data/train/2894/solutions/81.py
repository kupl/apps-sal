def triple_trouble(one, two, three):
    res = ""
    for x in range(len(one)):
        res += one[x]
        res += two[x]
        res += three[x]

    return res
