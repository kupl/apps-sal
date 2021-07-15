a=int(input())
for j in range(0,a):
 b=int(input())
 l1=list(map(int,input().split(" ")))
 l2=[]
 sum=0
 first=0
 count=0
 last=len(l1)-1
 while(first<=last):
  temp=0
  if(l1[first]<0):
   count+=1
   if(l1[last]>0):
    sum=sum+l1[last]
    temp=l1[first]
    l1[first]=l1[last]
    l1[last]=temp
    l2.append(first+1)
    l2.append(last+1)
    first+=1
    last-=1
   else:
    last-=1
  else:
   x=l1[first]
   sum=sum+l1[first]
   first+=1
 l2.sort()
 if(count>0):
  
  if(len(l2)==0):
   print("0")
   print(len(l2));
  
  else:
   print(sum)
   print(len(l2),end=" ")
  
  if(len(l2)==0):
   pass
  else:
   for k in range(0,len(l2)):
    if(k==len(l2)-1):
     print(l2[k])
    else:
     print(l2[k],end=" ")
   
 else:
  print(sum)
  print("0")
  
  
    
   
 
  
    
    
    
  
  
  
  
  

