
import math


def lcm(a):
    lm = a[0]
    for i in range(1, len(a)):
        lm = lm * a[i] // math.gcd(lm, a[i])
    return lm


t = int(input())
for T in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    r = int(input())
    lc = lcm(l)
    print(lc + r)
