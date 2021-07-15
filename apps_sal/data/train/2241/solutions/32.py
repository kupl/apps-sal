n, c = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
MOD = 10 ** 9 + 7

dp = [[0] * (c + 1) for i in range(n + 1)]
dp[0][0] = 1

ru = [[0] * 410 for i in range(410)]
for cnt in range(410):
    for x in range(409):
        ru[cnt][x + 1] += ru[cnt][x] + pow(x, cnt, MOD)
        ru[cnt][x + 1] %= MOD
      
for ni in range(n):
    for cnt in range(c + 1):
        for ci in range(cnt, c + 1):
            dp[ni + 1][ci] += (ru[cnt][b[ni] + 1] - ru[cnt][a[ni]]) * dp[ni][ci - cnt] 
            dp[ni + 1][ci] %= MOD
print(dp[-1][-1])
