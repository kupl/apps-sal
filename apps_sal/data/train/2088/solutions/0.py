n = int(input())
C = list(map(int, input().split()))

dp = [[0]*n for _ in range(n)]
for i in range(n) :
    dp[i][i] = 1

for i in range(n-2, -1, -1) :
    for j in range(i+1, n) :
        dp[i][j] = 1 + dp[i+1][j]
        if C[i] == C[i+1] : dp[i][j] = min( dp[i][j], 1 + (dp[i+2][j] if i+2 < n else 0) )
        for k in range(i+2, j) :
            if C[i] == C[k] : dp[i][j] = min( dp[i][j], dp[i+1][k-1] + dp[k+1][j] )
        if C[i] == C[j] and j-i > 1:
            dp[i][j] = min( dp[i][j], dp[i+1][j-1] )

print( dp[0][n-1] )

            
        

