def gimme(input_array):
    sortedlst = []
    unsortedlst = []
    for i in input_array:
        unsortedlst.append(i)
        sortedlst.append(i)
    sortedlst.sort()
    biggestNumber = sortedlst[1]
    return unsortedlst.index(biggestNumber)
