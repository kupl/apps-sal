import math


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


for _ in range(int(input())):
    n, m = list(map(int, input().split(" ")))
    p = list(map(int, input().split(" ")))
    g = p[0]
    for i in range(1, m):
        g = gcd(g, p[i])

    if g > n:
        maxEl = 1
        for i in range(n, 0, -1):
            if g % i == 0:
                maxEl = i
                break
        print(n - maxEl)
    else:
        print(n - g)
