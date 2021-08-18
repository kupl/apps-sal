def triple_trouble(one, two, three):
    res = len(one)
    l = ''
    for i in range(res):
        result = one[i] + two[i] + three[i]
        l = l + result
    return l
