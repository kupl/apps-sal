# editorial解法
from math import sqrt
Q = int(input())
for i in range(Q):
    A, B = list(map(int, input().split(" ")))
    if A == B or A + 1 == B:
        print((2 * A - 2))
        continue

    mul = A * B
    C = int(sqrt(mul))
    if C * C == mul:
        C -= 1
    if (C + 1) * C < mul:
        print(((2 * C) - 1))  # (A-1) + (2*C - A)
    else:
        print(((2 * C) - 2))  # (A-1) + (2*C - A - 1)
