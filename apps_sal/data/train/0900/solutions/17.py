import math


def com():
    a = []
    p = 10
    m = 1000000007
    a.append(10)
    for i in range(1, 10):
        p = a[i - 1] % m
        p = p * 2 % m
        p = p % m
        a.append(p)
    return a


t = int(input())
m = 1000000007
while t > 0:
    k = int(input())
    c = 2 ** (k - 1)
    c = c % m
    c = c * 10
    c = c % m
    print(c)
    t -= 1
