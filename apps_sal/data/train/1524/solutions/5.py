t = eval(input(""))
 
while(t>0):
 n,k = list(map(int,input().split()))
 
 if(k==1):
  if(n==1):
   ans=k;
   print(ans)
   
 else:
  ans=k;
  n=n-1
  k=k-1
  p=1
  while(n>0):
   p=p*k
   p=p%1000000007
   n=n-1
  
  
  ans=(ans*p)%1000000007
 
  print(ans)
  
  
 t=t-1 
