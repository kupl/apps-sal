from sys import stdin, stdout, setrecursionlimit
from math import ceil
t = int(stdin.readline())
for _ in range(t):
    (n, d) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    c = a[:]
    for i in range(n):
        q = d // a[i]
        a[i] *= q
    for i in range(n - 1, 0, -1):
        if a[i] - a[i - 1] < 0:
            q = a[i] // c[i - 1]
            a[i - 1] = c[i - 1] * q
        elif a[i] - a[i - 1] > 1:
            q = a[i - 1] // c[i]
            a[i] = c[i] * (q + 1)
    print(a[0])
