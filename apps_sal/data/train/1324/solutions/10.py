for _ in range(int(input())):
 n,k=map(int,input().split())
 z=(k*(k+1))//2
 if z>n:
  print(-1)
 elif z==n:
  print(1)
 else:
  ans=1
  for i in range(1,int(n**0.5)+1,1):
   if n%i==0:
    if i>=z:
     ans=max(n//i,ans)
    elif n//i>=z:
     ans=max(i,ans)
  print(ans)
