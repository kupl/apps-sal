def for1(M,k):
 ret = 0.0
 x = k*k+0.0
 z=x
 for m in range(1,M):
  ret+=(M-m)/x
  x*=z
 return ret 
  
def for2(M,k):
 ret = 0.0
 x = k+0.0
 for m in range(1,M):
  ret+=(M-m)/x
  
  x*=k
 return ret 
  
def ans(M,N,K):

 return int(round(M*N+M*for2(N,K)+N*for2(M,K)+K*for1(M,K)*for1(N,K),0))
M,N,K = list(map(int,input().split()))
print(ans(M,N,K)) 

