import sys
input = sys.stdin.readline
(n, r1, r2, r3, d) = list(map(int, input().split()))
A = list(map(int, input().split()))
DP = [1 << 60] * n
DP2 = [1 << 60] * n
DP.append(0)
DP.append(0)
for i in range(n):
    DP[i] = min(DP[i], DP[i - 1] + r1 * A[i] + r3 + d)
    if i >= 1:
        DP2[i] = min(DP2[i], DP[i - 2] + min(r1 * (A[i - 1] + 1), r2) + min(r1 * (A[i] + 1), r2) + r1 * 2 + d * 4)
        DP2[i] = min(DP2[i], DP2[i - 1] + min(r1 * (A[i] + 1), r2) + r1 + d * 3)
        DP[i] = min(DP[i], DP2[i])
ANS = DP[n - 1] - d
last = r1 * A[n - 1] + r3
for i in range(1, n):
    last += d * 2
    last += min(r1 * (A[n - 1 - i] + 1), r2) + r1
    ANS = min(ANS, DP[n - 2 - i] + last)
print(ANS)
