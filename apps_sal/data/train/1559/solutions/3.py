mod=1000000007
t=eval(input())
while(t>0):
 flag=0
 n=eval(input())
 if(n>=4):
  if(n%2==0):
   flag=1

  ans=1
  base=3
  ans=pow(base,n,mod)
  if(flag==1):
   ans=ans+3
  else:
   ans=ans-3
  print(ans)
  
 else:
  if(n==1):
   print(4) 
  
  if(n==2):
   print(12)

  if(n==3):
   print(24)
 t=t-1

