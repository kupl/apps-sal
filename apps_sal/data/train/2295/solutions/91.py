import os
import sys

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

N = int(sys.stdin.readline())
A, B = list(zip(*[list(map(int, sys.stdin.readline().split())) for _ in range(N)]))

A = np.array(A, dtype=int)
B = np.array(B, dtype=int)
if np.all(A == B):
    print((0))
else:
    ans = A.sum() - B[A > B].min()
    print(ans)

