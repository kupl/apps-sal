import math


def swap(a, b):
    temp = a
    a = b
    b = temp


def xnor(a, b):
    if a < b:
        swap(a, b)
    if a == 0 and b == 0:
        return 1
    a_rem = 0
    b_rem = 0
    count = 0
    xnornum = 0
    while a != 0:
        a_rem = a & 1
        b_rem = b & 1
        if a_rem == b_rem:
            xnornum |= 1 << count
        count = count + 1
        a = a >> 1
        b = b >> 1
    return xnornum


t = int(input())
for o in range(t):
    (a, b, n) = map(int, input().split())
    c = a ^ b
    x = bin(c)
    x = x.split('b')
    x = x[1]
    x = len(x)
    d = xnor(a, b)
    p = [a, b, c]
    r = [a, b, d]
    k = n % 3 - 1
    if p[k] > r[k]:
        print(p[k])
    else:
        print(r[k])
