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


def nthXorFib(n, a, b):
    if n == 0:
        return a
    if n == 1:
        return b
    if n == 2:
        return a ^ b
    return nthXorFib(n % 3, a, b)


def nthXNorFib(n, a, b):
    if n == 0:
        return a
    if n == 1:
        return b
    if n == 2:
        return xnor(a, b)
    return nthXNorFib(n % 3, a, b)


for test in range(int(input())):
    (a, b, n) = map(int, input().split())
    print(max(nthXNorFib(n - 1, a, b), nthXorFib(n - 1, a, b)))
