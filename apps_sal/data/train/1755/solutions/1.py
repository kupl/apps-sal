
from collections import Counter


def getdDPTable(numList, sizeList, targetSum):

    numRows = sizeList + 1
    numCols = targetSum + 1

    dp = [[False for _ in range(numCols)] for _ in range(numRows)]
    parent = [[[] for _ in range(numCols)] for _ in range(numRows)]

    for r in range(numRows):
        dp[r][0] = True

    for r in range(1, numRows):
        for c in range(1, numCols):
            if c < numList[r - 1]:
                dp[r][c] = dp[r - 1][c]
                parent[r][c].append(tuple([r - 1, c]))
            else:
                alreadyBuilt = dp[r - 1][c]
                isInOriginalNumList = dp[r - 1][c - numList[r - 1]]
                dp[r][c] = alreadyBuilt or isInOriginalNumList

                if alreadyBuilt:
                    parent[r][c].append(tuple([r - 1, c]))
                if isInOriginalNumList:
                    parent[r][c].append(tuple([r - 1, c - numList[r - 1]]))

    return dp, parent, numRows, numCols


def getSubset(parent, numRows, targetSum):
    subset = []

    child = [tuple([numRows - 1, targetSum])]
    cRow, cCol = child[0][0], child[0][1]
    father = parent[numRows - 1][targetSum]

    while father:
        fRow = father[0][0]
        fCol = father[0][1]

        diff = cCol - fCol
        if diff != 0:
            subset.append(diff)

        cRow = fRow
        cCol = fCol
        father = parent[fRow][fCol]

    return subset


def getBestNum(dp, numList, targetSum, numRows):

    for j in range(targetSum, -1, -1):
        if dp[numRows - 1][j] == True:
            break

    return j


def splitlist(numList):

    sizeList = len(numList)

    targetSum = sum(numList) // 2
    dp, parent, numRows, numCols = getdDPTable(numList, sizeList, targetSum)

    foundSubset = dp[numRows - 1][targetSum]

    bestDiff = 0
    if foundSubset:
        subsetA = getSubset(parent, numRows, targetSum)
    else:
        newTargetSum = getBestNum(dp, numList, targetSum, numRows)
        dp, parent, numRows, numCols = getdDPTable(numList, sizeList, newTargetSum)
        subsetA = getSubset(parent, numRows, newTargetSum)

    c1 = Counter(numList)
    c2 = Counter(subsetA)
    diff = c1 - c2
    subsetB = list(diff.elements())

    return subsetA, subsetB
