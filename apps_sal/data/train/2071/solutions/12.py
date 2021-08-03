from functools import reduce
from collections import Counter
3

n = int(input())
x = Counter()
y = Counter()
points = Counter()
for i in range(n):
    point = list(map(int, input().split()))
    x[point[0]] += 1
    y[point[1]] += 1
    points[(point[0], point[1])] += 1


def getPairsNumber(n):
    return n * (n - 1) // 2


def getCounterPairsNumber(counter):
    return reduce(lambda s, n: s + getPairsNumber(n), list(counter.values()), 0)


s = getCounterPairsNumber(x) + getCounterPairsNumber(y) - getCounterPairsNumber(points)
print(s)
