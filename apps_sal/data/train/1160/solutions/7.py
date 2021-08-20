import math


def floorm(a, b):
    if a % b == 0:
        return a / b - 1
    else:
        return a / b


def ceilp(a, b):
    if a % b == 0:
        return a / b + 1
    else:
        return (a + 1) / b + 1


def calc(h, m, f):
    (l, r) = (0, 1234567890)
    for i in range(len(h) - 1):
        if i & 1:
            (u, v) = (i, i + 1)
        else:
            (u, v) = (i + 1, i)
        if f:
            (u, v) = (v, u)
        (H, M) = (h[u] - h[v], m[v] - m[u])
        if M > 0:
            r = min(floorm(H, M), r)
        elif M < 0:
            l = max(ceilp(H, M), l)
        elif H <= 0:
            return (-1, -1)
        if l > r:
            return (-1, -1)
    return (l, r)


def printerval(l, r):
    if r == 1234567890:
        r = 'Inf'
    print(l, r)


def doit():
    (n, h, m, a, t, al, ar) = (int(input()), [], [], [], [0], [], [])
    for i in range(n):
        h += [0]
        m += [0]
        a += [0]
    for i in range(n):
        (h[i], m[i]) = list(map(int, input().split()))
    if n == 1:
        print(1)
        print('0 Inf')
        return
    (l1, r1) = calc(h, m, 1)
    (l2, r2) = calc(h, m, 0)
    if l1 != -1 and l2 != -1:
        if l1 > l2:
            (l1, l2, r1, r2) = (l2, l1, r2, r1)
        if r1 + 1 == l2:
            print(1)
            printerval(l1, r2)
        else:
            print(2)
            printerval(l1, r1)
            printerval(l2, r2)
    elif l1 != -1:
        print(1)
        printerval(l1, r1)
    elif l2 != -1:
        print(1)
        printerval(l2, r2)
    else:
        print(0)


for cas in range(int(input())):
    doit()
