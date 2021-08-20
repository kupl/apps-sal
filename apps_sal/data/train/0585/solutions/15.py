import math


def gcdiv(l):
    l.sort()
    ans = math.gcd(l[0], l[1])
    i = 2
    while ans != 1 and i < len(l):
        ans = math.gcd(ans, l[i])
        i = i + 1
    return ans


def lf(gc, n):
    if gc < n:
        return gc
    out = n
    while out > 1:
        if gc % out == 0:
            return out
        out -= 1
    return out


t = int(input())
while t > 0:
    t -= 1
    (n, m) = list(map(int, input().split()))
    l1 = list([int(i) for i in input().split()])
    if len(l1) > 1:
        gc = gcdiv(l1)
    else:
        gc = l1[0]
    print(n - lf(gc, n))
