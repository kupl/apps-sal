import os
import sys
if os.getenv('LOCAL'):
    sys.stdin = open('_in.txt', 'r')
sys.setrecursionlimit(2147483647)
INF = float('inf')
IINF = 10 ** 18
MOD = 10 ** 9 + 7


def ModInt(mod):

    class _ModInt:

        def __init__(self, value):
            self.value = value % mod

        def __add__(self, other):
            if isinstance(other, _ModInt):
                return _ModInt(self.value + other.value)
            else:
                return _ModInt(self.value + other)

        def __sub__(self, other):
            if isinstance(other, _ModInt):
                return _ModInt(self.value - other.value)
            else:
                return _ModInt(self.value - other)

        def __radd__(self, other):
            return self.__add__(other)

        def __mul__(self, other):
            if isinstance(other, _ModInt):
                return _ModInt(self.value * other.value)
            else:
                return _ModInt(self.value * other)

        def __truediv__(self, other):
            raise NotImplementedError()

        def __repr__(self):
            return str(self.value)
    return _ModInt


MI = ModInt(MOD)
(N, C) = list(map(int, sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))


def solve():
    P = [[1] * (C + 1) for _ in range(max(B) + 1)]
    P[0] = [MI(0)] * (C + 1)
    for i in range(1, len(P)):
        for c in range(1, C + 1):
            P[i][c] = P[i][c - 1] * i
    cs = [[0] * (C + 1) for _ in range(max(B) + 1)]
    for c in range(C + 1):
        s = 0
        for i in range(len(P)):
            s += P[i][c]
            cs[i][c] = s
    S = [[0] * (C + 1) for _ in range(N)]
    for i in range(N):
        for c in range(C + 1):
            S[i][c] = cs[B[i]][c] - cs[A[i] - 1][c]
    dp = S[0][:]
    for i in range(1, N):
        for c in reversed(list(range(C + 1))):
            s = 0
            for j in range(c + 1):
                s += dp[c - j] * S[i][j]
            dp[c] = s
    return dp[-1]


print(solve())
