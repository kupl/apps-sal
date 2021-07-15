test=int(input())
for i in range(test):
 n=int(input())
 a=list(map(int,input().split()))
 b=[0]*(n+2)
 b[n-1]=1
 for i in range(n-2,-1,-1):
  if(a[i]*a[i+1]<0):
   b[i]=b[i+1]+1
  else:
   b[i]=1
 for i in range(n):
  print(b[i], end=' ')
 print() 
