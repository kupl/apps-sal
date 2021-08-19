def read():
    return list(map(int, input().split()))


n = int(input())
p = sorted([tuple(read()) for i in range(n)])
a = [0] * (n + 1)
b = [0] * (n + 1)
for i in range(1, n + 1):
    (a[i], b[i]) = p[i - 1]
a[0] = int(-10000000.0)
dp = [0] * (n + 1)
for i in range(1, n + 1):
    L = 0
    R = n + 1
    while R - L > 1:
        M = (L + R) // 2
        if a[i] - b[i] <= a[M]:
            R = M
        else:
            L = M
    dp[i] = dp[L] + 1
ans = n - max(dp)
print(ans)
