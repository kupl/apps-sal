t=int(input())
for i in range(t):
 n=int(input())
 l,b=list(map(int,input().split()))
 while n>0:
  if l>b:
   l-=b
  else:
   b-=l
  n-=1
 if l*b>0:
  print("Yes",l*b)
 else:
  print("No")
