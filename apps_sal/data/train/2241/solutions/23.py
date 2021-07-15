N,C=map(int,input().split())
A=[int(i) for i in input().split()]
B=[int(i) for i in input().split()]
mod=10**9+7
exponen=[[0 for j in range(401)]for i in range(401)]
for i in range(401):
    exponen[i][0]=1
    for j in range(400):
        exponen[i][j+1]=(exponen[i][j]*i)%mod
expsum=[[0 for j in range(401)] for i in range(402)]
for j in range(401):
    for i in range(401):
        expsum[i+1][j]=(expsum[i][j]+exponen[i][j])%mod
func=[[0 for j in range(C+1)] for i in range(N)]
dp=[[0 for j in range(C+1)] for i in range(N+1)]
dp[0][0]=1
for i in range(N):
    for j in range(C+1):
        func[i][j]=(expsum[B[i]+1][j]-expsum[A[i]][j])%mod
for i in range(N):
    for x in range(C+1):
        for y in range(C+1):
            if (x+y>C):
                continue
            dp[i+1][x+y]+=dp[i][x]*func[i][y]
            dp[i+1][x+y]%=mod
print(dp[N][C])
