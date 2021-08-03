mod = (10**9) + 7
n, m = list(map(int, input().split()))
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
dp = []
for i in range(n):
    dp += [[0] * m]
dp[-1][-1] = 1
for i in range(n - 2, -1, -1):
    dp[i][-1] = 1
    for j in range(m - 1):
        x = (a[i] + b[j]) - (b[j + 1])
        temp = 0
        for k in range(i + 1, n):
            if(a[k] >= x):
                temp += dp[k][j + 1]
        dp[i][j] = temp
ans = 0
for i in range(n):
    ans += dp[i][0]
print(ans % mod)
