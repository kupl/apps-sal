t=eval(input())
for i in range(t):
 n=eval(input())
 a=list(map(int,input().split()))
 f=0
 for i in range(1,n-1):
  if sum(a[0:i])==sum(a[i+1:]):
   
   f=i
   break
 if sum(a[1:])==0:
  print(0)
 elif sum(a[0:n-1])==0:
  print(n-1)
 elif f==0:
  print(-1)
 else:
  print(f)

