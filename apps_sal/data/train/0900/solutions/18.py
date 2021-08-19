# cook your dish here
import math


def com():
    a = []
    a.append(1)
    m = 1000000007
    for i in range(1, 1000000):
        p = a[i - 1] % m
        p = p * 2
        p = p % m
        a.append(p)
    return a


t = int(input())
a = com()
w = 10000000 - 1
m = 1000000007
while(t > 0):
    k = int(input())
    c = a[k - 1] * 10
    c = c % m
    c = int(c)
    print(c)
    t -= 1
