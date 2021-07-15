# cook your dish here
t=int(input())
while t:
 m,c,h=input().split()
 m=int(m)
 c=int(c)
 h=int(h)
 
 x=abs(c-h)
 
 if(x%3!=0):
  print("Yes")
 
 else:
  if(x//3>m):
   print("Yes")
  else:
   print("No")
  
 t-=1
