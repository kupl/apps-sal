
def transpose(amount, tab):
    resultTab = ['' for tabStr in tab]
    numChars = set(char for char in '0123456789')

    i = 0
    while i < len(tab[0]):
        for tabNum, tabStr in enumerate(tab):
            try:
                valStr = tabStr[i]

                if not (i > 0 and valStr in numChars and tabStr[i - 1] in numChars):

                    if valStr is not '-' and i + 1 < len(tabStr) and tabStr[i + 1] in numChars:
                        valStr += tabStr[i + 1]

                    val = int(valStr)
                    transposedVal = val + amount

                    if transposedVal > 22 or transposedVal < 0:
                        return 'Out of frets!'

                    resultTab[tabNum] += str(transposedVal)

            except ValueError:
                resultTab[tabNum] += tabStr[i]

        maxLineLength = max([len(s) for s in resultTab])
        minLineLength = min([len(s) for s in resultTab])

        shouldTrim = False
        if maxLineLength != minLineLength:
            shouldTrim = all([(len(s) == minLineLength or s[len(s) - 1] == '-') for s in resultTab])
            if shouldTrim:
                i += 1

        for resTabNum, resTabStr in enumerate(resultTab):
            if shouldTrim:
                resultTab[resTabNum] = (resTabStr)[0:minLineLength]
            resultTab[resTabNum] = (resTabStr + '-')[0:maxLineLength]

        i += 1

    return resultTab
