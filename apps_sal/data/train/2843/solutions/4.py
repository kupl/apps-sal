import sys
print(sys.getrecursionlimit())


def pack_bagpack(scores, weights, capacity):
    if capacity >= sum(weights):
        return sum(scores)
    print('{},{},{}'.format(scores, weights, capacity))
    items = [(i, j) for (i, j) in zip(scores, weights)]

    def fetchBestMax(toConsider, avail, memo={}):
        if (len(toConsider), avail) in memo:
            result = memo[len(toConsider), avail]
        elif toConsider == [] or avail == 0:
            result = (0, ())
        elif toConsider[0][1] > avail:
            result = fetchBestMax(toConsider[1:], avail, memo)
        else:
            nextItem = toConsider[0]
            (withVal, withToTake) = fetchBestMax(toConsider[1:], avail - nextItem[1], memo)
            withVal += nextItem[0]
            (withoutVal, withoutToTake) = fetchBestMax(toConsider[1:], avail, memo)
            if withVal > withoutVal:
                result = (withVal, withToTake + (nextItem,))
            else:
                result = (withoutVal, withoutToTake)
        memo[len(toConsider), avail] = result
        return result
    maxVal = fetchBestMax(items, capacity)
    print(('maxVal', maxVal))
    return maxVal[0]
