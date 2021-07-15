MOD=10**9+7
N,C=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
P=[[1] for _ in range(401)]
for _ in range(1,401):
    for i in range(1,401):
        P[i].append(P[i][-1]*i%MOD)
R=[[] for _ in range(N)]
for i,AB in enumerate(zip(A, B)):
    AA,BB=AB
    for a in range(401):
        tmp=0
        for x in range(AA,BB+1):
            tmp+=P[x][a]
            tmp%=MOD
        R[i].append(tmp)
dp=[[0]*(C+1) for _ in range(N+1)]
dp[0][0]=1
for n in range(1,N+1):
    for k in range(C+1):
        for l in range(k+1):
            dp[n][k]+=dp[n-1][k-l]*R[n-1][l]
            dp[n][k]%=MOD
print(dp[N][C])
