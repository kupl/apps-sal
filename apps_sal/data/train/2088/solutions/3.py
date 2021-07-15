n = int(input())
dp = [[None for j in range(n)] for i in range(n)]
cl = input().split(' ')
cl = [int(color) for color in cl]

for bias in range(0, n):
    for l in range(n-bias):
        r = l + bias
        loc = float('+inf')
        if bias == 0:
            dp[l][r] = 1
        elif bias == 1:
            if cl[l] == cl[r]:
                dp[l][r] = 1
            else:
                dp[l][r] = 2
        else:
            if cl[l] == cl[r]:
                loc = dp[l+1][r-1]
            for k in range(l, r):
                loc = min(loc, dp[l][k]+dp[k+1][r])
            dp[l][r] = loc

print(dp[0][n-1])

