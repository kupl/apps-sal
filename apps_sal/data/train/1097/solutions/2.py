# cook your code here
t=eval(input())
while(t):
 n=eval(input())
 l,b=list(map(int,input().split()))
 for i in range(n):
  if(l<b):
   b-=l;
  else:
   l-=b;
 if(l>0 and b>0):
  print("Yes",l*b)
 else:
  print("No")
 t=t-1
  

