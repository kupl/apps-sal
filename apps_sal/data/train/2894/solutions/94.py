def triple_trouble(one, two, three):
    res = []
    for i in range(len(one)):
        res.append(one[i] + two[i] + three[i])
    return ''.join(res)
