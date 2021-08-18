"""
@author: souradeep1999

"""

import math as ma


def num():
    return list(map(int, input().split()))


def nu():
    return int(input())


def li():
    return input().split()


def lli():
    return list(map(int, input().split()))


def fli():
    return [float(x) for x in input().split()]


t = nu()
for tt in range(t):
    n = nu()
    a = lli()
    a.sort()
    d = 1
    for i in range(1, n):
        if(a[i] != a[i - 1]):
            d = d + 1
    cnt = 0
    c = 1
    for i in range(1, n):
        if(a[i] == a[i - 1]):
            c = c + 1
        else:
            if(c % 2 == 0):
                cnt = cnt + 1
            c = 1
    if(c % 2 == 0):
        cnt = cnt + 1

    if(cnt % 2 == 1):
        d = d - 1

    print(d)
