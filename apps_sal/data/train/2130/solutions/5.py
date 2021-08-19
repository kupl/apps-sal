c = []
k = int(input())
for i in range(k):
    c.append(int(input()))
maxN = 1010
binomials = [[1], [1, 1]]
for i in range(2, maxN):
    binomials.append([1])
    for j in range(1, i):
        binomials[i].append((binomials[i - 1][j - 1] + binomials[i - 1][j]) % 1000000007)
    binomials[i].append(1)
dp = [1] * k
for i in range(1, k):
    dp[i] = dp[i - 1] * binomials[sum(c[:i + 1]) - 1][c[i] - 1] % 1000000007
print(dp[k - 1])
