# cook your dish here
t=int(input())
for _ in range(t):
 x,y,k,n=map(int,input().split())
 if(y > x):
  time=(n-y)//k
  yfinal=y+time*k
  xnet=x+time*k
  diff=yfinal-xnet
  if(diff % (2*k)==0):
   print("Yes")
  else:
   print("No")
 elif(x > y):
  time=(y-0)//k
  yfinal=y-time*k
  xnet=x-time*k
  diff=xnet-yfinal
  if(diff%(2*k)==0):
   print("Yes")
  else:
   print("No")
