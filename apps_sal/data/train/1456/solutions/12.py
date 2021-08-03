# cook your dish here
import math


def howmany(n):
    total = n * (n + 1) // 2
    a = 1
    while(a <= n):
        total = total - a * ((n - a) // (2 * a) + 1)
        total = total - 1
        a = a * 2
    return total


t = int(input())
for you in range(t):
    l = input().split()
    x = int(l[0])
    y = int(l[1])
    print(howmany(y) - howmany(x - 1))
