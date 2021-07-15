try:
 from math import sqrt
 t,x=list(map(int,input().split()))
 for _ in range(t):
  n=int(input())
  if(n<0):
   print("no")
  else:
   diff=(x/100)*n
   ans=int(sqrt(n))
   ans1=ans**2
   if(n-ans1<=diff):
    print("yes")
   else:
    print("no")
except:
 pass

