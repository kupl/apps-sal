import math


def getk(n):
    exp = (9 + 8 * n)**0.5
    exp -= 1
    exp = exp // 2
    return math.floor(exp)


t = int(input())
while(t):
    n = int(input())
    k = int(getk(n))
    offset = int(n - (k * (k + 1) // 2 - 1))
    if(offset == 0):
        offset = k
    print(offset - 1)
    t -= 1
