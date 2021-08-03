import math


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    x = a[0]
    for i in a:
        x = math.gcd(i, x)
    if x == 1:
        k = -1
    else:
        k = x
        x1 = x ** 0.5
        t = int(x1)
        for i in range(2, t + 1):
            if x % i == 0:
                k = i
                break
    print(k)


def __starting_point():
    t = int(input())
    while t != 0:
        solve()
        t -= 1


__starting_point()
