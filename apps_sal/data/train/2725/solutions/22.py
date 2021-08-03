def gimme(inputArray):
    return 3 - inputArray.index(min(inputArray)) - inputArray.index(max(inputArray))
