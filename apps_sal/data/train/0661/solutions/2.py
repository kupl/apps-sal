try:
 from math import sqrt
 t,x=list(map(int,input().split()))
 for _ in range(t):
  n=abs(int(input()))
  diff=(x/100)*n
  ans=int(sqrt(n))
  ans1=ans**2
  if(n-ans1<=diff):
   print("yes")
  else:
   print("no")
except:
 pass

