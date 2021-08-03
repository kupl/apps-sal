def totalAmountVisible(topNum, numOfSides):
    return sum(range(1, numOfSides + 1)) - (numOfSides - topNum + 1)
