try:
 
 t=int(input())
 for _ in range(t):
  n=int(input())
  count=0
  maxi=0
  for i in range(n):
   param=list(map(int,input().split()))
   s,p,v=param[0],param[1],param[2]
   s=s+1
   
   p=int(p/s)
   profit=v*p
  
   if(maxi<profit):
    maxi=profit
    count=i+1
  print(maxi)
except:
 pass
