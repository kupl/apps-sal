# cook your dish here
for _ in range(int(input())):
 
 n,p,q=list(map(int,input().split()))
 
 l=sorted(map(int,input().split()))
 ans=0
 if q==0:
  
  ans=0
  for amount in l:
   
   if amount<=p:
    p-=amount
    ans+=1
   if p==0:
    break
   
  print(ans)
  
 elif p==0:
  ans=0
  for amount in l:
   
   if amount%2==0:
    
    k=amount//2
    
    if k<=q:
     q-=k
     ans+=1
     
   if q==0:
    break
  
  print(ans)
  
  
 else:
  ans=0
  
  for amount in l:
   check=0
   while amount>0:
    
    if q>0 and amount>=2:
     amount-=2
     q-=1
    elif p>0:
     amount-=1
     p-=1
    if p==0 and q==0:
     break
    
   if amount==0:
    ans+=1
   
   if p==0 and q==0:
    break
   
  print(ans)
     
  
  
  
  
  
  

