import numpy as np
import sys
input = sys.stdin.readline

N = int(input())
X = np.array(input().split(), dtype=np.int64)
L = int(input())

U = N.bit_length()
next_x = []
next_x.append(np.searchsorted(X, X + L, side='right') - 1)
for i in range(U):
    next_x.append(next_x[i][next_x[i]])


def days(a, b):
    a -= 1
    b -= 1
    if b < a:
        a, b = b, a
    result = 0
    for n in range(U, -1, -1):
        c = next_x[n][a]
        if c < b:
            a = c
            result += 1 << n
    return result + 1


Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    print(days(a, b))
