def triple_trouble(one, two, three):
    result = ''
    for i in range(len(one)):
        segm = one[i] + two[i] + three[i]
        result += segm
    return result
