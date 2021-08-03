from sys import stdin, stdout
from itertools import accumulate


def Oddnos(l, r):
    smm = od[r - 1] - od[l]
    return smm & 1


def evennos(l, r):
    tot = (r - l - 1)
    smm = od[r - 1] - od[l]
    return ((tot - smm) & 1 == 0)


def getSum(l, r):
    return ps[r] - (ps[l - 1] if l >= 1 else 0)


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    od = list(accumulate([x & 1 for x in a]))
    ps = list(accumulate(a))
    d = {}
    mx = 0
    for i in range(n):
        if a[i] in d:
            prev = d[a[i]]
            if a[i] & 1 and Oddnos(prev, i):
                mx = max(mx, getSum(prev, i) - 2 * a[i])
            elif a[i] & 1 == 0 and evennos(prev, i):
                mx = max(mx, getSum(prev, i) - 2 * a[i])
        d[a[i]] = i
    print(mx)
