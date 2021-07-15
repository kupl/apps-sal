t=int(input())
while t>0:
 n=int(input())
 ans=1
 temp=1
 while temp<=n :
  ans=ans*(2*temp-1)
  temp=temp+1
 print(ans)
 t=t-1
