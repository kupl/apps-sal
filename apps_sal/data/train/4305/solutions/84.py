def order_weight(strng):
    codeList = []
    counter = 0
    finalString = ''

    wgList = strng.split(' ')

    for i in range(len(wgList)):
        for j in range(len(wgList[i])):
            counter = counter + int(wgList[i][j])
        codeList.append(counter)
        counter = 0

    finalList = sorted(list(zip(codeList, wgList)))

    for i in range(len(finalList)):
        finalString += finalList[i][1] + ' '
    return finalString[:-1]
