t=int(input())
for _ in range(t):
 n=int(input())
 c=str(n)
 a=list(c)
 i2=len(a)-1
 for i in range(len(a)-1,0,-1):
  if int(a[i])<int(a[i-1]):
   a[i-1]=int(a[i-1])-1
   i2=i-1
 if(a[0]!=0 and a[0]!="0"):
  for i in range(i2+1):
   print(a[i],end="")
  for i in range(i2+1,len(a)):
   print(9,end="")
 else:
  for i in range(1,i2):
   print(a[i],end="")
  for i in range(i2+1,len(a)):
   print(9,end="")
 print()
  
 

