def main():
    n = int(input())
    L = [None] * n
    for i in range(n):
        (x, y) = (int(x) for x in input().split())
        L[i] = (x, y)
    print(solver(L))


def solver(L):
    xDict = dict()
    yDict = dict()
    xyDict = dict()
    for (x, y) in L:
        if (x, y) in xyDict:
            xyDict[x, y] += 1
        else:
            xyDict[x, y] = 1
    repeats = 0
    for xy in xyDict:
        n = xyDict[xy]
        repeats += n * (n - 1) // 2
    for (x, y) in L:
        if x in xDict:
            xDict[x].append(y)
        else:
            xDict[x] = [y]
        if y in yDict:
            yDict[y].append(x)
        else:
            yDict[y] = [x]
    xSames = 0
    for x in xDict:
        n = len(xDict[x])
        xSames += n * (n - 1) // 2
    ySames = 0
    for y in yDict:
        n = len(yDict[y])
        ySames += n * (n - 1) // 2
    total = xSames + ySames - repeats
    return total


def almostEqual(x, y):
    return abs(x - y) < 10 ** (-8)


def distance(x1, y1, x2, y2):
    leg1 = abs(x1 - x2)
    leg2 = abs(y1 - y2)
    return (leg1 ** 2 + leg2 ** 2) ** 0.5


L = [(1, 1), (7, 5), (1, 5)]
L2 = [(0, 0), (0, 1), (0, 2), (-1, 1), (0, 1), (1, 1)]
L3 = [(0, 0), (0, 0), (0, 0)]
main()
