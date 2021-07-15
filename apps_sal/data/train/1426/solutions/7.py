for _ in range(int(input())):
 
 n, m = list(map(int,input().split()))
 
 l= list(map(int,input().split()))
 
 k=[0]*n
 ans=0
 
 for i in range(n):
  
  d,f,b = list(map(int,input().split()))
  
  if l[d-1]!=0:
   l[d-1]-=1
   k[i]=d
   ans+=f
  else:
   ans+=b
 j=0 
 for i in range(m):
  
  if l[i]!=0:
   
   while(j<n and l[i]>0):
    
    if k[j]==0:
     l[i]-=1
     k[j]=i+1
    j+=1
    
 print(ans)
 print(*k)
     
    
   
   
   
   
   
   
   
   
   
   

