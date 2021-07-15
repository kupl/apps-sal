for _ in range(int(input())):
 n=int(input())
 ar=[int(x) for x in input().split()]

 if n>62:
  print("NO")
 else:
  v=[]
  f=0
  for i in range(n):
   x=ar[i]
   if ar[i] not in v:
    v.append(ar[i])
   else:
    f=1
    break
   for j in range(i+1,n):
    x|=ar[j]
    if x in v:
     f=1
     break
    else:
     v.append(x)
   if f==1:
    break
  
  if f==1:
   print("NO")
  else:
   print("YES")
    
    
   
   
   
  
 
  
  

