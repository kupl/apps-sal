t = int(input())
for t in range(0,t):   
 q= list(map (int, input().rstrip().split()))
 n=q[0]
 u=q[1]
 d=q[2]
 e=0
 c=1
 a= list(map (int, input().rstrip().split()))
 for i in range(0,n-1):
  if(a[i+1]>a[i]):
   if(a[i+1]-a[i]<=u):
    c=c+1 
   else:
    break
  elif(a[i+1]==a[i]):
   c=c+1
  else: 
   if(a[i]-a[i+1]<=d):
    c=c+1 
   elif(a[i]-a[i+1]>d and e==0):
    c=c+1 
    e=1 
   else:
    break 
   
 print(c) 
    
   
 
    
    
    
   

