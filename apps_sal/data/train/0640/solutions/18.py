import math


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def __starting_point():
    t = int(input())
    for _ in range(t):
        li = list(map(int, input().split()))
        a = li[0]
        b = li[1]

        if a == b:
            print(0)
        else:
            l = lcm(a, b)
            res = (l / a) + (l / b)
            print(int(res - 2))


__starting_point()
