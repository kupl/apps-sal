n = int(input())
(*a,) = map(int, input().split())
dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
for i in range(n):
    dp[0][i] = a[i]
for i in range(1, n):
    for j in range(n - i + 1):
        dp[i][j] = dp[i - 1][j] ^ dp[i - 1][j + 1]
for i in range(1, n):
    for j in range(n - i):
        dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i - 1][j + 1])
for i in range(int(input())):
    (l, r) = map(int, input().split())
    print(dp[r - l][l - 1])
