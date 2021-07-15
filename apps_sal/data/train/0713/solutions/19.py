t=int(input())
for i in range(t):
 a=int(input())
 fa=input().split()
 b=int(input())
 fb=input().split()
 count=0
 k=0
 search=0
 x=[]
 y=[]
 for i in range(b):
  k=fb[i]
  if(k in fa):
   x.append(fa.index(k))
   y.append(fa.index(k))
 y.sort()
 if(x==y and len(x)==b):
  print("Yes")
 else:
  print("No")
   
   
   
  
 
  
 
  
 

