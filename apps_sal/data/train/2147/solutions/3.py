import sys
readline = sys.stdin.readline
INF = 10 ** 18
(N, r1, r2, r3, d) = map(int, readline().split())
A = list(map(int, readline().split()))
dp1 = [INF] * (N + 1)
dp2 = [INF] * (N + 1)
dp1[0] = -d
dp2 = -d
mj = INF
rr = r1 + r2
C = [0] * (N + 1)
for i in range(N):
    a = A[i]
    C[i + 1] = min(rr, (a + 2) * r1)
CC = C[:]
for i in range(1, N + 1):
    CC[i] += CC[i - 1]
for i in range(1, N + 1):
    a = A[i - 1]
    dp1[i] = dp2 + d + C[i]
    dp2 = min(dp2 + d + r1 * a + r3, CC[i] + 3 * d * i + mj)
    mj = min(mj, dp1[i] - 3 * i * d - CC[i])
ans = min(dp2, 2 * d + dp1[-1])
ans = min(ans, dp1[N - 1] + 3 * d + C[N])
zz = min(r1 * A[-1] + r3, 2 * d + min(rr, (A[-1] + 2) * r1))
for i in range(1, N):
    ans = min(ans, dp1[i] + 2 * (N - i) * d + zz + CC[N - 1] - CC[i])
print(ans)
