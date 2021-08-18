from collections import Counter


import math as mt

MAXN = 100001

spf = [0 for i in range(MAXN)]


def sieve():
    spf[1] = 1
    for i in range(2, MAXN):

        spf[i] = i

    for i in range(4, MAXN, 2):
        spf[i] = 2

    for i in range(3, mt.ceil(mt.sqrt(MAXN))):

        if (spf[i] == i):

            for j in range(i * i, MAXN, i):

                if (spf[j] == j):
                    spf[j] = i


def getFactorization(x):
    ret = list()
    while (x != 1):
        ret.append(spf[x])
        x = x // spf[x]

    return ret.pop()


sieve()


t = int(input())

for test in range(t):
    n = int(input())
    A = tuple(map(int, input().split()))
    li = []
    mx = 1
    mx_li = []
    for a in A:
        li.append(getFactorization(a))

    c = Counter(li)
    for key in c:
        if c[key] > mx:
            mx_li = [key]
            mx = c[key]
        elif c[key] == mx:
            mx_li.append(key)

    print(max(mx_li))
