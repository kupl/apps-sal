from collections import Counter
from math import factorial


def nc3(n):
    a = factorial(n)
    b = factorial(n - 3)
    return a / (b * 6)


def rem(s):
    t = -1
    x = -1
    for i in range(len(s)):
        if s[i][0] > 2:
            if s[i][0] > 3:
                ch = (nc3(s[i][0]) - nc3(s[i][0] - 1)) / s[i][1]
            else:
                ch = 1 / s[i][1]
            if t < ch:
                t = ch
                x = i
    return x


t = int(input())
for x in range(t):
    (n, c, k) = map(int, input().split())
    l = {}
    for i in range(n):
        (a, b, e) = map(int, input().split())
        if e in l:
            l[e].append(a)
        else:
            l[e] = []
            l[e].append(a)
    v = list(map(int, input().split()))
    s = []
    for i in range(1, c + 1):
        if i in l:
            s += [[len(l[i]), v[i - 1]]]
    while True:
        ma = rem(s)
        if s[ma][1] > k:
            break
        else:
            s[ma][0] -= 1
            k = k - s[ma][1]
    re = 0
    for i in s:
        if i[0] > 2:
            re = re + nc3(i[0])
    print(int(re))
