# cook your dish here
for _ in range(int(input())):
 n,k=map(int,input().split())
 s=input()
 if(n==k):
  print("both")
 else:
  x=0
  y=0
  for i in s:
   if(i.islower()):
    x=x+1
   else:
    y=y+1
  if(k>=x and k>=y):
   print("both")
  elif(k>=y):
   print("chef")
  elif(k>=x):
   print("brother")
  else:
   print("none")
