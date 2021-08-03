
def transpose(amount, tab):
    resultTab = ['' for tabStr in tab]
    numChars = set(char for char in '0123456789')

    i = 0
    while i < len(tab[0]):
        for tabNum, tabStr in enumerate(tab):
            try:
                valStr = tabStr[i]

                # Are we looking at the second character of a two character number
                if not (i > 0 and valStr in numChars and tabStr[i - 1] in numChars):

                    # If the next character is a number to complete a two character number
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
            # This happens if the input string had a two character number that went down to a one
            # character number after the transpose
            shouldTrim = all([(len(s) == minLineLength or s[len(s) - 1] == '-') for s in resultTab])
            if shouldTrim:
                i += 1

        for resTabNum, resTabStr in enumerate(resultTab):
            if shouldTrim:
                resultTab[resTabNum] = (resTabStr)[0:minLineLength]
            resultTab[resTabNum] = (resTabStr + '-')[0:maxLineLength]

        i += 1

    return resultTab
