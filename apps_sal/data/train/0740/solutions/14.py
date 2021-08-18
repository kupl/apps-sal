from math import *
t = int(input())
while t > 0:
    t -= 1
    n, m, k = list(map(int, input().split()))
    a = []
    b = []
    ll = k * 4
    for i in range(k):
        d = [int(x) for x in input().split()]
        a.append(d)
        d = d[::-1]
        b.append(d)
    a.sort()
    b.sort()

    for i in range(1, len(a)):
        if a[i][0] == a[i - 1][0] and abs(a[i][1] - a[i - 1][1]) == 1:
            ll -= 2
    for i in range(1, len(b)):
        if b[i][0] == b[i - 1][0] and abs(b[i][1] - b[i - 1][1]) == 1:
            ll -= 2
    print(ll)
