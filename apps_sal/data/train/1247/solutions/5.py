
import sys


def getSum(BITree, index):
    sum = 0
    while (index > 0):
        sum += BITree[index]
        index -= index & (-index)
    return sum


def updateBIT(BITree, n, index, val):
    while (index <= n):
        BITree[index] += val
        index += index & (-index)


def getInvCount(arr, n):
    invcount = 0
    maxElement = max(arr)
    BIT = [0] * (maxElement + 1)
    for i in range(1, maxElement + 1):
        BIT[i] = 0
    for i in range(n - 1, -1, -1):
        invcount += getSum(BIT, arr[i] - 1)
        updateBIT(BIT, maxElement, arr[i], 1)
    return invcount


input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    l = [int(i) for i in input().split()]
    f = 1
    sm = 0
    for x in range(k):
        mat = []
        li = []
        le = 0
        c = {}
        for y in range(x, n, k):
            mat.append(l[y])
            li.append(y + 1)
            le += 1
            c[l[y]] = 1
        for y in range(x, n, k):
            if c.get(y + 1, -1) == -1:
                f = 0
                break
        else:
            sm += getInvCount(mat, le)
    if f == 0:
        print(-1)
    else:
        print(sm)
