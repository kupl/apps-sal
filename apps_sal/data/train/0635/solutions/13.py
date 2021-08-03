# cook your dish here
n, k = list(map(int, input().split()))
x = list(map(int, input().split()))
l = [0 for i in range(100001)]
for i in x:
    l[i] += 1
l = list([a for a in l if a != 0])
# print(l)
k = min(k, len(l))
dp = [[0 for i in range(len(l) + 1)] for j in range(k)]
for i in range(1, len(l) + 1):
    dp[0][i] = dp[0][i - 1] + l[i - 1]
# print(dp)
ans = dp[0][len(l)] + 1
for i in range(1, k):
    for j in range(1, len(l) + 1):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1] * l[j - 1]) % 1000000007
    ans = (ans + dp[i][len(l)]) % 1000000007
# print(dp)
print(ans)
