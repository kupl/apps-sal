from decimal import *
getcontext().prec = 1
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = []
    i = 0
    b = []
    while i < n:
        x, y = list(map(int, input().split()))
        a.append(x + y)
        b.append(x - y)
        i += 1
    a.sort()
    b.sort()
    m = 1000000007
    for i in range(1, n):
        k = abs(a[i] - a[i - 1])
        l = abs(b[i] - b[i - 1])
        m = min(m, k, l)
    print(Decimal(m / 2))
