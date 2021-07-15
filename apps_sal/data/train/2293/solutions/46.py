import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))


N = I()
A = LI()

# 高速ゼータ変換

dp = [[0]*(N+1) for _ in range(1<<N)]
for i in range(1<<N):
    for j in range(N+1):
        if j == 0:
            dp[i][j] = A[i]
            continue
        if not i&(1<<(j-1)):
            dp[i][j] = dp[i][j-1]
        else:
            a,b = divmod(dp[i][j-1],1<<30)
            c,d = divmod(dp[i&~(1<<(j-1))][j-1],1<<30)
            X = [a,b,c,d]
            X.sort(reverse=True)
            dp[i][j] = (X[1]<<30)+X[0]

ans = 0
for i in range(1,1<<N):
    a,b = divmod(dp[i][-1],1<<30)
    ans = max(ans,a+b)
    print(ans)

