N,C=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
DP=[[0]*(C+1) for i in range(N+1)]
DP[0][0]=1
mod=10**9+7
X=[[0] for i in range(401)]
for i in range(401):
  for j in range(401):
    X[i].append((X[i][j]+pow(j,i,mod))%mod)
for i in range(N):
  for j in range(C+1):
    for k in range(j+1):
      DP[i+1][j]=(DP[i][j-k]*(X[k][B[i]+1]-X[k][A[i]])+DP[i+1][j])%mod
print(DP[N][C])
