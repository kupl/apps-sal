from math import atan
t = int(input())


def f(a, b, x, y):
    m = (b - x) / y
    n = (a - x) / y
    return atan(m) - atan(n)


for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    (p, q) = map(int, input().split())
    k = n // 2
    s = 0
    for j in range(k):
        s = s + f(a[j], a[n - 1 - j], p, q)
    if s < 0:
        s = -s
    print(s)
