import math


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


t = int(input())
for i in range(0, t):
    k = int(input())
    a = list(map(int, input().split()))
    c = a[0]
    for j in range(1, len(a)):
        c = gcd(c, a[j])
    if c == 1:
        print(k)
    else:
        print(-1)
