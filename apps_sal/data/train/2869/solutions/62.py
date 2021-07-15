def distinct(arr):
    newA = []
    for el in arr:
        if not el in newA:
            newA.append(el)
    return newA
