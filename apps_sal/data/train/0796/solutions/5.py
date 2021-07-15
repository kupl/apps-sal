for _ in range(eval(input())):
 n=eval(input())
 a=list(map(int,input().split()))
 b=[1]*n
 for i in range(n-2,-1,-1):
  if a[i+1]<0 and a[i]>0 or a[i+1]>0 and a[i]<0:
   b[i]=b[i]+b[i+1]
 for i in range(n):
  print(b[i], end=' ')
 print() 
