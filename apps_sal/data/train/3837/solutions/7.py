def coutingLine(downLine, rightCount):
    upLine = [rightCount]
    for itemDLine in downLine:
        upLine.append(itemDLine - upLine[-1])
    return upLine

def swapList(currentList):
    return list(currentList[-item] for item in range(1, len(currentList)+1))

def reverse(right):
    pyramide = [[right[0]]]
    for index in range(0, len(right) - 1):
        pyramide.append(coutingLine(pyramide[-1], right[index + 1]))
        
    return swapList(pyramide[-1])
    




