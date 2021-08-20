def distinct(seq):
    uniqueList = []
    for elem in seq:
        if elem not in uniqueList:
            uniqueList.append(elem)
    return uniqueList
