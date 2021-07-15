import sys
def multiply(matrix1,matrix2,mod):
 ans=[[-1 for i in range(len(matrix2[0]))] for _ in range(len(matrix1))]
 #print(ans,'before')
 for i in range(len(matrix1)):
  for j in range(len(matrix2[0])):
   s=0
   k=0
   while k<len(matrix1[0]):
    s+=(matrix1[i][k]*matrix2[k][j])%mod
    k+=1
   ans[i][j]=(s%mod)
 #print(ans,'ans')
 return ans
def power(a,b,mod):
 res=[[1,0],[0,1]]
 #print(res,'res')
 for i in range(len(a)):
  for j in range(len(a[0])):
   a[i][j]=a[i][j]%mod
 #print(a,'a')
 while b>0:
  if (b&1):
   res=multiply(res,a,mod)
  b=b>>1
  a=multiply(a,a,mod)
 return res
t=int(sys.stdin.readline())
mod=10**9+7
for _ in range(t):
 n,m=list(map(int,sys.stdin.readline().split()))
 base=[[m],[0]]
 a=[[m-1,m-1],[1,0]]
 #print(base,'base')
 #print(a,'a')
 ans=power(a,n-1,mod)
 #print(ans,'ans')
 ans=multiply(ans,base,mod)
 print((ans[0][0]+ans[1][0])%mod)
 
   

