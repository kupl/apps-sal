from sys import stdout
from bisect import *


def fun(n, f):
    ct = 1
    while n % f == 0:
        ct += 1
        n //= f
    return ct


N = 1000009
l = [0] * N
a = [0] * N
b = [1] * N
for i in range(N):
    l[i] = i
for i in range(2, N):
    if l[i] > 0:
        a[i] += 1
        b[i] += 1
        j = i + i
        while j < N:
            l[j] = 0
            a[j] += 1
            b[j] *= fun(j, i)
            j += i
arr = []
for i in range(2, 10000):
    if l[i] > 0:
        arr.append(i)
lis = [0] * 10001
for i in arr:
    for j in arr:
        if i + 2 * j <= 10000:
            lis[i + 2 * j] += 1
for i in range(int(input())):
    print(lis[int(input())])
