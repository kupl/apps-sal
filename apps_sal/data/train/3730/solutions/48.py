def capitalize(s):
    newString, secondString = "", ""
    for i, j in enumerate(s):
        if i % 2 == 0:
            newString += j.upper()
        else:
            newString += j
    for i, j in enumerate(s):
        if i % 2 == 0:
            secondString += j
        else:
            secondString += j.upper()
    return [newString, secondString]
