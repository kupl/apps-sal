def triple_trouble(one, two, three):
    newStr = ''
    for i in range(len(one)):
        newStr += one[i] + two[i] + three[i]
    return newStr
