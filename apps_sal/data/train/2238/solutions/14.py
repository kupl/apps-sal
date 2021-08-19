import sys


def L(x):
    return x.bit_length() if x > 0 else 1


n = int(input())
while n > 0:
    n -= 1
    (l, r) = list(map(int, sys.stdin.readline().split()))
    a = 0
    while L(l) == L(r) and r > 0:
        u = 1 << L(r) - 1
        l -= u
        r -= u
        a += u
    u = 1 << L(r) - 1
    if u + u - 1 == r and r > 1:
        u <<= 1
    print(a + u - 1)
