from datetime import datetime


class dicta(dict):
    def __init__(self, *args, **kwargs):
        super(dicta, self).__init__(*args, **kwargs)
        self.__dict__ = self


# -----------------------------------------------------------------------------
START_TIME = datetime.now()


def debug(**kwargs):

    return
    diff = str(datetime.now() - START_TIME)
    for key, value in list(kwargs.items()):
        if isinstance(value, list):
            print(diff, key + ':')
            for itemKey, item in enumerate(value):
                print('\t\t\t', str(itemKey) + ': ' + str(item))
        elif isinstance(value, dict):
            print(diff, key + ':')
            for itemKey, item in list(value.items()):
                print('\t\t\t', itemKey + ': ' + str(item))
        else:
            print(diff, key + ': ' + str(value))

# -----------------------------------------------------------------------------


def printResult(result):
    if isinstance(result, list):
        print(*result)
    else:
        print(result)

# -----------------------------------------------------------------------------


def main():
    debug(status='started')
    noOfTests = int(input())

    for i in range(noOfTests):
        result = runATest(i)
        if isinstance(result, tuple):
            for line in result:
                printResult(line)
        else:
            printResult(result)
        if noOfTests > 1:
            debug(status='-------------------- finished Test#' + str(i + 1) + '                 --------------------')
    debug(status='finished')


def runATest(_testIndex):

    [count, refTotal] = [int(x) for x in input().split()]

    aList = [int(x) for x in input().split()]
    factors = findFactors(refTotal, count)
    # debug(refTotal=refTotal, count=count, factors=factors)

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

    reqSum = int(refTotal / size)
    sumList = [0] * (reqSum + 1)

    sumSize = sum(aList[:size])
    if sumSize <= reqSum:
        sumList[sumSize] += 1
    debug()

    rightOffset = size - 1
    for i in range(1, count + 1 - size):
        # debug(window=i)
        sumSize = sumSize - aList[i - 1] + aList[i + rightOffset]
        if sumSize <= reqSum:
            sumList[sumSize] += 1

    total = 0
    for i in range(0, (reqSum + 1) // 2 + 1):
        # debug(summing=f'{i}, {-1 - i}')
        subTotal = sumList[i] * sumList[-1 - i]
        if i != reqSum - i:
            subTotal *= 2
        total += subTotal

    debug(reqSum=reqSum, size=size, total=total, sumList=sumList)
    return total


main()
