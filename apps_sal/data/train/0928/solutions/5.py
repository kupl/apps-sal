import math
t = int(input())


def CountSquares(b):
    return math.floor(math.sqrt(b))


for i in range(t):
    n = int(input())
    l = 0
    l = CountSquares(n)
    c = 0
    for i in range(2, l + 1):
        if i % 3 == 0:
            c += 1
    print(l - c)
