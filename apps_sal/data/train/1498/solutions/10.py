# cook your dish here
import math


def printDivisors(n, X, l):
    list = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if (n % i == 0):
            if (n / i == i):
                list.append(i)
                a = 0
            else:
                list.append(i)
                list.append(int(n / i))

    for i in list[::-1]:
        if(i - X >= 0):
            l.append(i)


T = int(input())
for _ in range(T):
    H, X, Y = list(map(int, input().split()))
    l = []
    printDivisors(H - 1, X, l)
    mv = 2 * H
    for i in l:
        a = (i - X) // Y
        if(a * Y == (i - X)):
            v = ((H - 1) // i) + a
            if(v < mv):
                mv = v

    if(mv > H):
        print(-1)

    else:
        print(mv)
