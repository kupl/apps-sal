import math


def xnor(a, b):
    if a < b:
        (a, b) = (b, a)
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


for _ in range(int(input())):
    (a, b, n) = map(int, input().split())
    X = [a, b, a ^ b]
    E = [a, b, xnor(a, b)]
    i = (n - 1) % 3
    print(max(X[i], E[i]))
