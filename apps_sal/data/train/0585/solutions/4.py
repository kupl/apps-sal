import math


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def maxfact(g, n):
    i = 1
    maxf = None
    while i * i <= g:
        if g % i == 0:
            if i <= n:
                maxf = i
            if math.floor(g / i) <= n:
                maxf = math.floor(g / i)
                break
        i = i + 1
    return maxf


t = int(input())
while t > 0:
    t = t - 1
    [n, m] = [int(x) for x in input().split(' ')]
    spells = [int(x) for x in input().split(' ')]
    g = spells[0]
    for i in range(1, m):
        g = gcd(g, spells[i])
    print(n - maxfact(g, n))
