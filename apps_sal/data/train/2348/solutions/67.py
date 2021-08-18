import bisect
from math import log2, ceil


def reachN(i0, n):
    if n == 0:
        return i0
    maxbit = ceil(log2(n))
    kL = []
    for i in range(maxbit + 1):
        if n >> i & 1:
            kL.append(i)
    i = i0
    for k in kL[::-1]:
        if start < goal:
            i = dp[k][i]
        else:
            i = dpInv[k][i]
    return i


def fun(n):
    if start < goal:
        return reachN(start, n) >= goal
    else:
        return reachN(start, n) <= goal


def binMin(l, r):
    if r - l == 1:
        return r
    m = (l + r) // 2
    if fun(m):
        r = m
    else:
        l = m
    return binMin(l, r)


N = int(input())
xL = [-float('inf')] + [int(i) for i in input().split()]
Lmax = int(input())

kmax = ceil(log2(len(xL) - 2))
dp = [[len(xL) - 1] * (N + 1) for _ in range(kmax + 1)]
for i in range(1, N + 1):
    dp[0][i] = bisect.bisect_right(xL, xL[i] + Lmax) - 1
for k in range(1, kmax + 1):
    for i in range(1, N):
        dp[k][i] = dp[k - 1][dp[k - 1][i]]

dpInv = [[1] * (N + 1) for _ in range(kmax + 1)]
for i in range(N, 1, -1):
    dpInv[0][i] = bisect.bisect_left(xL, xL[i] - Lmax)
for k in range(1, kmax + 1):
    for i in range(N, 1, -1):
        dpInv[k][i] = dpInv[k - 1][dpInv[k - 1][i]]

Q = int(input())
for _ in range(Q):
    start, goal = list(map(int, input().split()))
    ans = binMin(0, abs(goal - start))
    print(ans)
