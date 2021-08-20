import math


def Left(i):
    return 2 * i


def Right(i):
    return 2 * i + 1


def levelOf(x):
    return int(math.floor(math.log10(x) / math.log10(2) + 1))


def treeProduct(numList, n, i):
    if levelOf(i) == n:
        return numList[i]
    else:
        tpl = treeProduct(numList, n, Left(i))
        tpr = treeProduct(numList, n, Right(i))
        if tpl > tpr:
            return numList[i] * tpl
        else:
            return numList[i] * tpr


def main():
    n = int(input())
    while n != 0:
        line = '-1 ' + str(input())
        s = line.split()
        num = [int(e) for e in s]
        print(int(treeProduct(num, n, 1) % 1000000007))
        n = int(input())


def __starting_point():
    main()


__starting_point()
