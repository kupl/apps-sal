import numpy as np
import sys
input = sys.stdin.readline

N = int(input())
X = np.array(input().split(), dtype=np.int64)
L = int(input())

U = N.bit_length()
# 各ホテルから、2^n回でどこまで行けるか
next_x = []
next_x.append((np.searchsorted(X, X + L, side='right') - 1).tolist())
for i in range(U):
    next_x.append([next_x[i][next_x[i][n]] for n in range(N)])


def days(a, b):
    a -= 1
    b -= 1
    if b < a:
        a, b = b, a
    # 到着できない範囲で最大限進む
    result = 0
    for n in range(U, -1, -1):
        c = next_x[n][a]
        if c < b:
            a = c
            result += 1 << n
    return result + 1


Q = int(input())
for _ in range(Q):
    a, b = list(map(int, input().split()))
    print((days(a, b)))
