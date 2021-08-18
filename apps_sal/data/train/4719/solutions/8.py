def sort_array(a):
    lenList = len(a)

    if lenList == 0:
        return []

    evenNums, oddNums = [], []
    evenNumLoc, oddNumLoc = [], []

    for i in range(0, lenList, 1):
        if a[i] % 2 == 0:
            evenNums.append(a[i])
            evenNumLoc.append(i)
        else:
            oddNums.append(a[i])
            oddNumLoc.append(i)

    evenNums.sort(reverse=True)
    oddNums.sort()

    sortedList = [0 for _ in range(lenList)]
    totalNumEvens = len(evenNums)
    totalNumOdds = len(oddNums)

    for i in range(0, totalNumEvens, 1):
        sortedList[evenNumLoc[i]] = evenNums[i]

    for i in range(0, totalNumOdds, 1):
        sortedList[oddNumLoc[i]] = oddNums[i]

    return sortedList
