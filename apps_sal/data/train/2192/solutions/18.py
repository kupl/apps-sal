n = int(input())
dp = [0] * 1000007
majak = [0] * 1000007
q = 1000007
p = 0
for i in range(n):
    (a, b) = list(map(int, input().split()))
    q = min(q, a)
    majak[a] = b
dp[q] = 1
ma = 1
for i in range(q + 1, 1000003, 1):
    if majak[i] == 0:
        dp[i] = dp[i - 1]
    else:
        dp[i] = dp[i - majak[i] - 1] + 1
        ma = max(ma, dp[i])
print(n - ma)
