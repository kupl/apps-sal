try:
 n,a=map(int,input().split())
 while a>0:
  if n%10==0:
   n//=10
  else:
   n-=1
  a-=1
 print(n)
except:
 pass
