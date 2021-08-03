import math


def lcm(x, y, z):
    s = x * y
    p = s // math.gcd(x, y)
    s = p * z
    p = s // math.gcd(p, z)
    return p


for _ in range(int(input())):
    n = int(input())
    x, y, z = list(map(int, input().split()))
    z = lcm(x, y, z)
    x = n * 24 // z
    print(x)
