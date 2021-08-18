import math


def LCMofArray(a):
    lcm = a[0]
    for i in range(1, len(a)):
        lcm = lcm * a[i] // math.gcd(lcm, a[i])
    return lcm


for T in range(int(input())):
    n = int(input())
    N = list(map(int, input().split()))
    r = int(input())
    print(LCMofArray(N) + r)
