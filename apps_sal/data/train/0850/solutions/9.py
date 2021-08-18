import random
from math import gcd


def gh(a, b):
    if len(a) and len(b):
        x = a[0]
        y = b[0]
        for i in a[1:]:
            x = gcd(x, i)
        for i in b[1:]:
            y = gcd(y, i)
        return x + y
    return 0


def abc(l):
    s = 2**len(l)
    i = 0
    d = "{0:0" + str(len(l)) + "b}"
    ans = 0
    while i < s:
        x = d.format(i)
        a = []
        b = []
        for j in range(len(l)):
            if x[j] == '1':
                a.append(l[j])
            else:
                b.append(l[j])
        ans = max(ans, gh(a, b))
        i += 1
    return ans


for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    d = {}
    for i in l:
        try:
            d[i] += 1
        except:
            d[i] = 1
    x = list(d.keys())
    x.sort()
    if len(x) == 1:
        print(2 * l[0])
    else:
        ans = x[-1]
        c = x[0]
        for i in range(len(x) - 1):
            c = gcd(c, x[i])
        vy = ans + c
        ans = x[-2]
        c = 0
        for i in range(len(x) - 2):
            c = gcd(c, x[i])
        c = gcd(c, x[-1])
        vx = ans + c
        print(max(vx, vy))
