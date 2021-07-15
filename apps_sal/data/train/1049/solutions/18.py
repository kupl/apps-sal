# cook your dish here
while True:
 try:
  
  t=int(input())
  h=1 
  while(h<=t):
   n,k=list(map(int,input().split()))
   lis=list(map(int,input().split()))
 
   unique_data=[]
   for i in lis:
    if i not in unique_data:
     unique_data.append(i)
   #print(unique_data)
 
   maxi=0
   lis2=[]
   for i in range(0,n-k+1):
    lis2=lis[i:i+k]
    #print(lis2)
    t=0
    for i in set(lis2):
     if i in unique_data:
      t+=1
   #print(t)
    if(t==len(unique_data)):
     if(sum(lis2)>maxi):
      maxi=sum(lis2)

   print(maxi)
   h+=1
 except:
  break
    
  
  

