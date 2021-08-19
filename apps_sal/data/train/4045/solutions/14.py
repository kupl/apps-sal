def number(a):
    lineCount = 1
    lineList = []
    while a:
        lineList.append(str(lineCount) + ': ' + a.pop(0))
        lineCount += 1
    return lineList
