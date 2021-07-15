# cook your dish here
T=int(input())
for _ in range(T):
 X,Y=map(int,input().split())
 diff=abs(X-Y)
 if(X>Y):
  if (diff%2==0):
   ans=1
  else:
   ans=2
   
 elif (X<Y):
  if (diff%2!=0):
   ans=1

  elif (diff%4==0):
   ans=3

  else:
   ans=2

 else:
  ans=0

 print(ans)
