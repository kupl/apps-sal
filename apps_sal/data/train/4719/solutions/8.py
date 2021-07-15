def sort_array(a):
    lenList = len(a)

    if lenList ==0:
        return []

    evenNums, oddNums = [], []
    evenNumLoc, oddNumLoc = [],[]

    #Walk through the given list of numbers, and store even numbers (and 
    #their index loc); same for odds 
    for i in range(0, lenList, 1):
        if a[i]%2==0:
            evenNums.append(a[i])   #save even number
            evenNumLoc.append(i)    #save even number index location
        else:
            oddNums.append(a[i])    #save odd number
            oddNumLoc.append(i)     #save odd number location

    evenNums.sort(reverse = True)   #decending order for evens
    oddNums.sort()                  #ascending order for odds

    #pre allocate the list so we can store via direct access
    sortedList = [0 for _ in range(lenList)]
    totalNumEvens = len(evenNums)
    totalNumOdds  = len(oddNums)

    #Store the sorted even numbers at the indicies where they were located in the original list
    for i in range(0, totalNumEvens, 1):
        sortedList[evenNumLoc[i]] = evenNums[i]

    #Store the sorted odd numbers at the indicies where they were located in the original list
    for i in range(0, totalNumOdds, 1):
        sortedList[oddNumLoc[i]] = oddNums[i]

    return sortedList

#end function

