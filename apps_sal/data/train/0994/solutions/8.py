from datetime import datetime

START_TIME = datetime.now()


def debug(*args, **kwargs):
    return


def printResult(result):
    if isinstance(result, list):
        print(*result)
    else:
        print(result)


def main():
    debug('started')
    noOfTests = int(input())

    for i in range(noOfTests):
        result = runATest(i)
        if isinstance(result, tuple):
            for line in result:
                printResult(line)
        else:
            printResult(result)
    debug('finished')


def runATest(_testIndex):

    [count, refTotal] = [int(x) for x in input().split()]

    aList = [int(x) for x in input().split()]
    factors = findFactors(refTotal, count)
    debug(factors=factors)

    total = 0
    for factor in factors:
        total += countSquaresOfSize(aList, refTotal, count, factor)
    return total


def findFactors(refTotal, maxFactor):

    outList = [1]

    for i in range(2, int(refTotal / 2) + 1):
        if i > maxFactor:
            break
        if refTotal % i == 0:
            outList.append(i)

    if refTotal <= maxFactor:
        outList.append(refTotal)

    return outList


def countSquaresOfSize(aList, refTotal, count, size):

    reqTotal = int(refTotal / size)
    maxLen = count + 1 - size
    total = 0

    for i in range(maxLen):
        for j in range(maxLen):
            if countSquaresAtPointOfSize(aList, reqTotal, size, i, j):
                total += 1

    debug('completed size', size=size, total=total)
    return total


def countSquaresAtPointOfSize(aList, reqTotal, size, i, j):

    total = 0

    for k in range(size):
        total += aList[i + k] + aList[j + k]

    debug(i=i, j=j, size=size, total=total, reqTotal=reqTotal)
    return total == reqTotal


main()
