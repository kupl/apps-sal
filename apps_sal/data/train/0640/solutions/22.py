from math import gcd


def lcm(x, y):
    return x * y // (gcd(x, y))


for i in range(int(input())):
    n, m = list(map(int, input().split()))
    k = lcm(n, m)
    print(k // n + k // m - 2)
