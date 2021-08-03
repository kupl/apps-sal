import math


def hello(x, n):
    xPn = (x / 100) * n
    sqr = math.sqrt(n)
    sqr = math.floor(sqr)
    sqr = sqr**2
    if(abs(n - sqr) <= xPn):
        return "yes"
    else:
        return "no"


def __starting_point():
    [t, x] = list(map(int, input().split()))
    r = []
    for i in range(t):
        n = int(input())
        r.append(hello(x, n))
    print(*r, sep="\n")


__starting_point()
