for _ in range(int(input())):
 n,k=map(int,input().split())
 if n<=k:
  div=k//n
  rem=k%n
  if rem: 
   maxx=div+1
   minn=div
  else: 
   maxx=div
   minn=div
 else:
  maxx=1
  minn=0
 print(minn)
