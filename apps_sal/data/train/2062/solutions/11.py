N,A,B,C,D=list(map(int,input().split()))
mod=10**9+7

F=[1]*(N+1)
for i in range(1,N+1):
  F[i]=F[i-1]*(i)%mod
def power(x,y):
  if y==0:
    return 1
  elif y==1:
    return x%mod
  elif y%2==0:
    return power(x,y//2)**2%mod
  else:
    return (power(x,y//2)**2)*x%mod

invF=[1]*(N+1)
invF[N]=power(F[N],mod-2)
for i in range(0,N)[::-1]:
  invF[i]=(invF[i+1]*(i+1))%mod
invp=[[0]*(N+1) for i in range(N+1)]
for i in range(N+1):  
  for k in range(N+1):
    if k==0:
      invp[i][k]=1
    else:
      invp[i][k]=(invp[i][k-1]*invF[i])%mod
dp=[[0]*(N+1) for i in range(B-A+2)]
dp[0][0]=1
for i in range(A,B+1):
  for j in range(N+1):
    dp[i-A+1][j]=dp[i-A][j]
    for k in range(C,min(D,j//i)+1):
      dp[i-A+1][j]+=(dp[i-A][j-k*i]*F[N-j+k*i]*invF[N-j]*invp[i][k]*invF[k])%mod
      dp[i-A+1][j]%=mod
    
print(((dp[B-A+1][N])%mod))


        
  


    

