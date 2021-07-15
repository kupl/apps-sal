
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cost = 0

    dp = [[] for val in range(2*n+1)]
    cnt = [0]*(n*2+1)
    dp[0].extend([ 0 for val in range(n*2+1) ])

    for val in a:
     if val<=2*n: cnt[val]+=1
     else: cost+=1
 
    for i in range(1, n*2+1):
     rn = n*2//i
     for j in range(0, rn+1):
      dp[i].extend( [ dp[i-1][j] + abs(cnt[i]-j) ] )
     for j in range(rn-1, -1, -1):
      dp[i][j] = min(dp[i][j], dp[i][j+1])
 
    print( cost+min( dp[2*n][0], dp[2*n][1]) )


