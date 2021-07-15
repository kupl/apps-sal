t=int(input())
for _ in range(t):
 n,k,x,y=list(map(int,input().strip().split()))
 
 if x==y:
  print(n,n)
  
 else:
 
  if x<y:
   ans1=(x+(n-y),n)
   ans2=(n,x+(n-y))
   ans3=(y-x,0)
   ans4=(0,y-x)
  
  elif y<x:
   ans1=(n,y+(n-x))
   ans2=(y+(n-x),n)
   ans3=(0,x-y)
   ans4=(x-y,0)
  
  if k%4==1:
   print(ans1[0],ans1[1])
  elif k%4==2:
   print(ans2[0],ans2[1])
  elif k%4==3:
   print(ans3[0],ans3[1])
  else:
   print(ans4[0],ans4[1])
  
  


