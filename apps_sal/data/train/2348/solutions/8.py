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
    # print(kL)
    i = i0
    for k in kL[::-1]:
        i = dp[k][i]  # ; print('norm', i)
    return i


def fun(n):
    return reachN(start, n) >= goal


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
xL = [-float('inf')] + [int(i) for i in input().split()]  # ; print(xL)
Lmax = int(input())

kmax = ceil(log2(len(xL) - 2))  # ; print(kmax)
dp = [[len(xL) - 1] * (N + 1) for _ in range(kmax + 1)]
for i in range(1, N + 1):
    dp[0][i] = bisect.bisect_right(xL, xL[i] + Lmax) - 1
# print2(dp)
for k in range(1, kmax + 1):
    for i in range(1, N):
        dp[k][i] = dp[k - 1][dp[k - 1][i]]
#print2(dp); print()

Q = int(input())
for _ in range(Q):
    start, goal = list(map(int, input().split()))
    if start > goal:
        start, goal = goal, start
    ans = binMin(0, goal - start)
    print(ans)
