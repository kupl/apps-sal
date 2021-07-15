t=int(input())
for i in range(0,t):
 n=int(input())
 x=4*n
 ans=2
 m=n+1
 tem=0
 if(n%2==0):
  ans=(n/2)*8
 elif(n%4==3):
  ans=n
 else:
  val=(n+3)/4
  ans=2+(val-1)*8
 print(ans)
