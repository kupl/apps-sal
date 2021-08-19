def triple_trouble(one, two, three):
    oneL = list(one)
    twoL = list(two)
    threeL = list(three)
    returnArr = []
    for i in range(len(oneL)):
        returnArr.append(oneL[i])
        returnArr.append(twoL[i])
        returnArr.append(threeL[i])
    return ''.join(returnArr)
