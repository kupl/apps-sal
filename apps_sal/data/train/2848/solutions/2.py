import itertools


def find(lst, targetSum):
    lenList = len(lst)

    combWithReplacementList = []
    for chooseR in range(1, lenList + 1):
        combsChooseR = itertools.combinations_with_replacement(lst, chooseR)
        combWithReplacementList.append(list(combsChooseR))

    totalFound = 0
    for col in combWithReplacementList:
        for combChoice in col:
            if (sum(combChoice)) == targetSum:
                totalFound += 1

    return totalFound
